# -*- coding: utf-8 -*-
# TODO: update docstring
"""Defines the Book views
"""
from django.utils.text import slugify
from rest_framework import generics
from rest_framework import serializers
from rest_framework.permissions import IsAdminUser
from api.models.book import Book
from api.serializers.book import Serializer
from api.serializers.history import HistorySerializer


class ItemView(generics.RetrieveAPIView):
    # TODO: update docstring
    """    Provides access to the DELETE, GET, PATCH and PUT requests for a given ID.
    """
    queryset = Book.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer
    lookup_field = "id"


class ItemEditView(generics.UpdateAPIView):
    # TODO: update docstring
    """Provides access to the PATCH and PUT requests for a given ID.
    """
    permission_classes = (IsAdminUser,)
    queryset = Book.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer
    lookup_field = "id"


class ItemDeleteView(generics.DestroyAPIView):
    # TODO: update docstring
    """Provides access to the DELETE requests for a given ID.
    """
    permission_classes = (IsAdminUser,)
    queryset = Book.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer
    lookup_field = "id"


class ListView(generics.ListAPIView):
    # TODO: update docstring
    """Provides access to the GET request for a list of all book objects.
    """
    queryset = Book.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer


class CreateView(generics.CreateAPIView):
    # TODO: update docstring
    """Provides access to the POST request for creating book objects.
    """
    permission_classes = (IsAdminUser,)
    queryset = Book.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer

    def create(self, request, *args, **kwargs):  # pylint: disable=unused-argument
        # TODO: update docstring
        """create
        """
        name = request.data['name']
        item_id = slugify(name)

        queryset = Book.objects.filter(id=item_id)  # pylint: disable=no-member

        if queryset.count() != 0:
            detail = 'A Book entry already exists with the id '+item_id
            raise serializers.ValidationError(detail)

        return super().create(request, *args, **kwargs)


class BookHistoryView(generics.RetrieveAPIView):
    # TODO: update docstring
    """Get org history by name
    """
    serializer_class = HistorySerializer
    queryset = Book.objects.all()  # pylint: disable=no-member
    lookup_field = "id"
