# -*- coding: utf-8 -*-
"""
Defines the BookFormat views
"""
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.models.book_format import BookFormat
from api.models.book_format import Serializer

class ItemView(generics.RetrieveUpdateDestroyAPIView):
    '''
    Provides access to the DELETE, GET, PATCH and PUT requests for a given ID.
    '''
    permission_classes = (IsAuthenticated,)
    queryset = BookFormat.book_formats.all()
    serializer_class = Serializer
    lookup_field = "id"

class ListView(generics.ListAPIView):
    '''    
    Provides access to the GET request for a list of all book-format objects.
    '''
    queryset = BookFormat.book_formats.all()
    serializer_class = Serializer

class CreateView(generics.CreateAPIView):
    '''
    Provides access to the POST request for creating book-format objects.
    '''
    permission_classes = (IsAuthenticated,)
    queryset = BookFormat.book_formats.all()
    serializer_class = Serializer
