# -*- coding: utf-8 -*-
"""
Defines the BookFormat views
"""
from django.utils.text import slugify
from rest_framework import generics
from rest_framework import serializers
from rest_framework.permissions import IsAdminUser
from api.models.book_format import BookFormat
from api.serializers.book_format import Serializer
from api.serializers.history import HistorySerializer


class ItemView(generics.RetrieveAPIView): # pylint: disable=too-many-ancestors
    """
    Provides access to the GET method for a given BookFormat ID.
    """
    queryset = BookFormat.objects.all() # pylint: disable=no-member
    serializer_class = Serializer
    lookup_field = "id"

class ItemEditView(generics.UpdateAPIView): # pylint: disable=too-many-ancestors
    """
    Provides access to the PATCH and PUT methods for a given BookFormat ID.
    """
    permission_classes = (IsAdminUser,)
    queryset = BookFormat.objects.all() # pylint: disable=no-member
    serializer_class = Serializer
    lookup_field = "id"

class ItemDeleteView(generics.DestroyAPIView): # pylint: disable=too-many-ancestors
    """
    Provides access to the DELETE method for a given BookFormat ID.
    """
    permission_classes = (IsAdminUser,)
    queryset = BookFormat.objects.all() # pylint: disable=no-member
    serializer_class = Serializer
    lookup_field = "id"

class ListView(generics.ListAPIView):
    """
    Provides access to the GET method for a list of all BookFormat objects.
    """
    queryset = BookFormat.objects.all() # pylint: disable=no-member
    serializer_class = Serializer

class CreateView(generics.CreateAPIView):
    """
     Provides access to the POST method for creating BookFormat objects.
    """
    permission_classes = (IsAdminUser,)
    queryset = BookFormat.objects.all() # pylint: disable=no-member
    serializer_class = Serializer

    def create(self, request, *args, **kwargs):
        """
        create
        """
        name = request.data['name']
        item_id = slugify(name)

        queryset = BookFormat.objects.filter(id=item_id) # pylint: disable=no-member

        if queryset.count() != 0:
            detail = 'A Book Format entry already exists with the id '+item_id
            raise serializers.ValidationError(detail)

        return super(CreateView, self).create(request, *args, **kwargs)

class BookFormatHistoryView(generics.RetrieveAPIView):
    """
    Get book BookFormat history by id
    """
    serializer_class = HistorySerializer
    queryset = BookFormat.objects.all() # pylint: disable=no-member
    lookup_field = "id"
