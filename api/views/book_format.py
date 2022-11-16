# -*- coding: utf-8 -*-
# TODO: update docstring
"""Defines the BookFormat views
"""
from django.utils.text import slugify
from rest_framework import generics
from rest_framework import serializers
from rest_framework.permissions import IsAdminUser
from api.models.book_format import BookFormat
from api.serializers.book_format import Serializer
from api.serializers.history import HistorySerializer


class ItemView(generics.RetrieveAPIView):
    # TODO: update docstring
    """Provides access to the GET method for a given BookFormat ID.
    """
    queryset = BookFormat.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer
    lookup_field = "id"


class ItemEditView(generics.UpdateAPIView):
    # TODO: update docstring
    """Provides access to the PATCH and PUT methods for a given BookFormat ID.
    """
    permission_classes = (IsAdminUser,)
    queryset = BookFormat.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer
    lookup_field = "id"


class ItemDeleteView(generics.DestroyAPIView):
    # TODO: update docstring
    """Provides access to the DELETE method for a given BookFormat ID.
    """
    permission_classes = (IsAdminUser,)
    queryset = BookFormat.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer
    lookup_field = "id"


class ListView(generics.ListAPIView):
    # TODO: update docstring
    """Provides access to the GET method for a list of all BookFormat objects.
    """
    queryset = BookFormat.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer


class CreateView(generics.CreateAPIView):
    # TODO: update docstring
    """Provides access to the POST method for creating BookFormat objects.
    """
    permission_classes = (IsAdminUser,)
    queryset = BookFormat.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer

    def create(self, request, *args, **kwargs):  # pylint: disable=unused-argument
        # TODO: update docstring
        """create
        """
        name = request.data['name']
        item_id = slugify(name)

        queryset = BookFormat.objects.filter(  # pylint: disable=no-member
            id=item_id)

        if queryset.count() != 0:
            detail = 'A Book Format entry already exists with the id '+item_id
            raise serializers.ValidationError(detail)

        return super().create(request, *args, **kwargs)


class BookFormatHistoryView(generics.RetrieveAPIView):
    # TODO: update docstring
    """Get book BookFormat history by id
    """
    serializer_class = HistorySerializer
    queryset = BookFormat.objects.all()  # pylint: disable=no-member
    lookup_field = "id"
