# -*- coding: utf-8 -*-
"""
Defines the Schema views
"""
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.models.schema import Schema
from api.models.schema import DocumentSerializer
from api.models.schema import HrefSerializer
from api.models.schema import Serializer

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

class ItemVersionView(MultipleFieldLookupMixin, generics.RetrieveUpdateDestroyAPIView):
    '''
    Provides access to the DELETE, GET, PATCH and PUT requests for a given ID and Version.
    '''
    permission_classes = (IsAuthenticated,)
    queryset = Schema.schemas.all()
    serializer_class = HrefSerializer
    lookup_fields = ('id', 'version')

class DocumentVersionView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    '''
    Returns the document object in json format for a given ID and Version.
    '''
    queryset = Schema.schemas.all()
    serializer_class = DocumentSerializer
    lookup_fields = ('id', 'version')

class ListView(generics.ListAPIView):
    '''
    Provides access to the GET request for a list of all schema objects.
    '''
    queryset = Schema.schemas.all()
    serializer_class = HrefSerializer

class CreateView(generics.CreateAPIView):
    '''
    Provides access to the POST request for creating schema objects.
    '''
    permission_classes = (IsAuthenticated,)
    queryset = Schema.schemas.all()
    serializer_class = Serializer

class ItemView(generics.RetrieveAPIView):
    '''
    Provides access to the GET request for a given ID.
    '''
    permission_classes = (IsAuthenticated,)
    queryset = Schema.schemas.all()
    serializer_class = Serializer
    lookup_field = "id"
