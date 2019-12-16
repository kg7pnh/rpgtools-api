# -*- coding: utf-8 -*-
"""
Defines the GameSystem views
"""
from django.utils.text import slugify
from rest_framework import generics
from rest_framework import serializers
from rest_framework.permissions import IsAdminUser
from api.models.game_system import GameSystem
from api.serializers.game_system import Serializer
# from api.serializers.game_system import HyperLinkedSerializer
from api.serializers.history import HistorySerializer


class ItemView(generics.RetrieveAPIView): # pylint: disable=too-many-ancestors
    """
    Provides access to the DELETE, GET, PATCH and PUT requests for a given game_system ID.
    """
    queryset = GameSystem.objects.all() # pylint: disable=no-member
    # serializer_class = HyperLinkedSerializer
    serializer_class = Serializer
    lookup_field = "id"

class ItemEditView(generics.UpdateAPIView): # pylint: disable=too-many-ancestors
    """
    Provides access to the PATCH and PUT requests for a given game_system ID.
    """
    permission_classes = (IsAdminUser,)
    queryset = GameSystem.objects.all() # pylint: disable=no-member
    serializer_class = Serializer
    lookup_field = "id"

class ItemDeleteView(generics.DestroyAPIView): # pylint: disable=too-many-ancestors
    """
    Provides access to the DELETE request for a given game_system ID.
    """
    permission_classes = (IsAdminUser,)
    queryset = GameSystem.objects.all() # pylint: disable=no-member
    serializer_class = Serializer
    lookup_field = "id"

class ListView(generics.ListAPIView):
    """
    Provides access to the GET request for a list of all game_system objects.
    """
    queryset = GameSystem.objects.all() # pylint: disable=no-member
    serializer_class = Serializer

class CreateView(generics.CreateAPIView):
    """
     Provides access to the POST request for creating game_system objects.
    """
    permission_classes = (IsAdminUser,)
    queryset = GameSystem.objects.all() # pylint: disable=no-member
    serializer_class = Serializer

    def create(self, request, *args, **kwargs):
        name = request.data['name']
        item_id = slugify(name)

        queryset = GameSystem.objects.filter(id=item_id) # pylint: disable=no-member

        if queryset.count() != 0:
            detail = 'A Game System entry already exists with the id '+item_id
            raise serializers.ValidationError(detail)

        return super(CreateView, self).create(request, *args, **kwargs)

class GameSystemHistoryView(generics.RetrieveAPIView):
    """
    Get game system history by id
    """
    serializer_class = HistorySerializer
    queryset = GameSystem.objects.all() # pylint: disable=no-member
    lookup_field = "id"
