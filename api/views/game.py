# -*- coding: utf-8 -*-
"""
Defines the Game views
"""
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.models.game import Game
from api.models.game import Serializer

class MultipleFieldLookupMixin(): #pylint: disable=too-few-public-methods
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
        return get_object_or_404(queryset, **filter) #pylint: disable=undefined-variable

class ItemVersionView(MultipleFieldLookupMixin, generics.RetrieveUpdateDestroyAPIView):
    '''
    Provides access to the DELETE, GET, PATCH and PUT requests for a given ID and Version.
    '''
    permission_classes = (IsAuthenticated,)
    queryset = Game.games.all()
    serializer_class = Serializer
    lookup_fields = ('id', 'version')

class ItemView(generics.RetrieveAPIView):
    '''
    Provides access to the GET request for a given ID.
    '''
    permission_classes = (IsAuthenticated,)
    queryset = Game.games.all()
    serializer_class = Serializer
    lookup_field = "id"

class ListView(generics.ListAPIView):
    '''
    Provides access to the GET request for a list of all game objects.
    '''
    queryset = Game.games.all()
    serializer_class = Serializer

class CreateView(generics.CreateAPIView):
    '''
     Provides access to the POST request for creating game objects.
    '''
    permission_classes = (IsAuthenticated,)
    queryset = Game.games.all()
    serializer_class = Serializer
