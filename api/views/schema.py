# -*- coding: utf-8 -*-
"""
Defines the Schema views
"""
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from api.models.schema import Schema
from api.serializers.schema import DocumentSerializer
from api.serializers.schema import HrefSerializer
from api.serializers.schema import Serializer
from api.serializers.history import HistorySerializer

class MultipleFieldLookupMixin(): # pylint: disable=too-few-public-methods
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """
    def get_object(self):
        """
        get_object
        """
        queryset = self.get_queryset()  # Get the base queryset
        queryset = self.filter_queryset(queryset)
        filter = {} # pylint: disable=redefined-builtin
        for field in self.lookup_fields:
            # if self.kwargs[field]:  # Ignore empty fields.
            filter[field] = self.kwargs[field]
        return get_object_or_404(queryset, **filter) # pylint: disable=undefined-variable

class ItemVersionView(MultipleFieldLookupMixin, generics.RetrieveAPIView): # pylint: disable=too-many-ancestors
    """
    Provides access to the GET method for a given Schema ID and Version.
    """
    queryset = Schema.objects.all() # pylint: disable=no-member
    serializer_class = HrefSerializer
    lookup_fields = ('id', 'version')

class ItemEditView(MultipleFieldLookupMixin, generics.UpdateAPIView): # pylint: disable=too-many-ancestors
    """
    Provides access to the PATCH and PUT methods for a given Schema ID and Version.
    """
    permission_classes = (IsAdminUser,)
    queryset = Schema.objects.all() # pylint: disable=no-member
    serializer_class = Serializer
    lookup_fields = ('id', 'version')

    def update(self, request, *args, **kwargs): # pylint: disable=useless-super-delegation
        return super(ItemEditView, self).update(request, *args, **kwargs) # pylint: disable=no-member

class ItemDeleteView(MultipleFieldLookupMixin, generics.DestroyAPIView): # pylint: disable=too-many-ancestors
    """
    Provides access to the DELETE method for a given Schema ID and Version.
    """
    permission_classes = (IsAdminUser,)
    queryset = Schema.objects.all() # pylint: disable=no-member
    serializer_class = Serializer
    lookup_fields = ('id', 'version')

class DocumentVersionView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    """
    Returns the document object in json format for a given Schema ID and Version.
    """
    queryset = Schema.objects.all() # pylint: disable=no-member
    serializer_class = DocumentSerializer
    lookup_fields = ('id', 'version')

class ListView(generics.ListAPIView):
    """
    Provides access to the GET method for a list of all Schema objects.
    """
    queryset = Schema.objects.all() # pylint: disable=no-member
    serializer_class = Serializer

class CreateView(generics.CreateAPIView):
    """
    Provides access to the POST method for creating Schema objects.
    """
    permission_classes = (IsAdminUser,)
    queryset = Schema.objects.all() # pylint: disable=no-member
    serializer_class = Serializer

    def create(self, request, *args, **kwargs):
        name = request.data['name']
        item_id = slugify(name)
        version = 1

        queryset = Schema.objects.filter(id=item_id) # pylint: disable=no-member

        high_version = version
        if queryset.count() != 0:
            for entry in queryset:
                if entry.version > high_version:
                    high_version = entry.version
            version = high_version + 1

        request.data["version"] = version

        return super(CreateView, self).create(request, *args, **kwargs)

class ItemView(generics.RetrieveAPIView):
    """
    Provides access to the GET request for a given ID.
    """
    queryset = Schema.objects.all() # pylint: disable=no-member
    serializer_class = Serializer
    lookup_field = "id"

class SchemaHistoryView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    """
    Get Schema history by ID and Version
    """
    serializer_class = HistorySerializer
    queryset = Schema.objects.all() # pylint: disable=no-member
    lookup_fields = ('id', 'version')
