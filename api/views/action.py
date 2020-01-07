# -*- coding: utf-8 -*-
"""
Defines the BookFormat views
"""
from django.utils.text import slugify
from rest_framework import generics
from rest_framework import serializers
from rest_framework.permissions import IsAdminUser
from api.models.action import Action
from api.models.action import Serializer

class ItemView(generics.RetrieveAPIView): # pylint: disable=too-many-ancestors
    """
    Provides access to the GET method for a given Action ID.
    """
    queryset = Action.objects.all() # pylint: disable=no-member
    serializer_class = Serializer
    lookup_field = "id"

class ItemEditView(generics.UpdateAPIView): # pylint: disable=too-many-ancestors
    """
    Provides access to the PATCH and PUT methods for a given Action ID.
    """
    permission_classes = (IsAdminUser,)
    queryset = Action.objects.all() # pylint: disable=no-member
    serializer_class = Serializer
    lookup_field = "id"

class ItemDeleteView(generics.DestroyAPIView): # pylint: disable=too-many-ancestors
    """
    Provides access to the DELETE method for a given Action ID.
    """
    permission_classes = (IsAdminUser,)
    queryset = Action.objects.all() # pylint: disable=no-member
    serializer_class = Serializer
    lookup_field = "id"

class ListView(generics.ListAPIView):
    """
    Provides access to the GET method for a list of all Action objects.
    """
    queryset = Action.objects.all() # pylint: disable=no-member
    serializer_class = Serializer

class CreateView(generics.CreateAPIView):
    """
     Provides access to the POST method for creating Action objects.
    """
    permission_classes = (IsAdminUser,)
    queryset = Action.objects.all() # pylint: disable=no-member
    serializer_class = Serializer

    def create(self, request, *args, **kwargs):
        name = request.data['name']
        item_id = slugify(name)

        queryset = Action.objects.filter(id=item_id) # pylint: disable=no-member

        if queryset.count() != 0:
            detail = 'An Action entry already exists with the id '+item_id
            raise serializers.ValidationError(detail)

        return super(CreateView, self).create(request, *args, **kwargs)
