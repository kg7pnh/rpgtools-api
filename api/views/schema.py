# -*- coding: utf-8 -*-
"""
Defines the Schema views
"""
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import serializers
from rest_framework.permissions import IsAdminUser
from api.models.schema import Schema
from api.models.schema import DocumentSerializer
from api.models.schema import HrefSerializer
from api.models.schema import Serializer
from api.permissions.admin import IsAdminOrReadOnly

class MultipleFieldLookupMixin(): # pylint: disable=too-few-public-methods
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """
    def get_object(self):
        '''
        get_object
        '''
        queryset = self.get_queryset()  # Get the base queryset
        queryset = self.filter_queryset(queryset)
        filter = {} # pylint: disable=redefined-builtin
        for field in self.lookup_fields:
            if self.kwargs[field]:  # Ignore empty fields.
                filter[field] = self.kwargs[field]
        return get_object_or_404(queryset, **filter) # pylint: disable=undefined-variable

class ItemVersionView(MultipleFieldLookupMixin, generics.RetrieveUpdateDestroyAPIView): # pylint: disable=too-many-ancestors
    '''
    Provides access to the DELETE, GET, PATCH and PUT requests for a given ID and Version.
    '''
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Schema.objects.all()
    serializer_class = HrefSerializer
    lookup_fields = ('id', 'version')

    def update(self, request, *args, **kwargs):
        
        print('****DEBUG****')
        print(request.data)
        print('****DEBUG****')
        return super(ItemVersionView, self).update(request, *args, **kwargs)

class DocumentVersionView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    '''
    Returns the document object in json format for a given ID and Version.
    '''
    queryset = Schema.objects.all()
    serializer_class = DocumentSerializer
    lookup_fields = ('id', 'version')

class ListView(generics.ListAPIView):
    '''
    Provides access to the GET request for a list of all schema objects.
    '''
    queryset = Schema.objects.all()
    serializer_class = HrefSerializer

class CreateView(generics.CreateAPIView):
    '''
    Provides access to the POST request for creating schema objects.
    '''
    permission_classes = (IsAdminUser,)
    queryset = Schema.objects.all()
    serializer_class = Serializer

    def create(self, request, *args, **kwargs):
        name = request.data['name']
        id = slugify(name) # pylint: disable=redefined-builtin, invalid-name

        queryset = Schema.objects.filter(id=id)

        if queryset.count() != 0:
            high_version = 1
            for e in queryset:
                if e.version > high_version:
                    high_version = e.version

            request.data["version"] = high_version + 1

            # detail = 'A Book entry already exists with the id '+id
            # raise serializers.ValidationError(detail)

        return super(CreateView, self).create(request, *args, **kwargs)

class ItemView(generics.RetrieveAPIView):
    '''
    Provides access to the GET request for a given ID.
    '''
    queryset = Schema.objects.all()
    serializer_class = Serializer
    lookup_field = "id"
