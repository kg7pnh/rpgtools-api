# -*- coding: utf-8 -*-
# TODO: update docstring
"""Defines the Book views
"""
from django.utils.text import slugify
from rest_framework import generics
from rest_framework import serializers
from rest_framework.permissions import IsAdminUser
from api.models.contributor import Contributor
from api.models.person import Person
from api.models.person import concat_name
from api.serializers.person import Serializer
from api.serializers.history import HistorySerializer


class ItemView(generics.RetrieveAPIView):
    """Provides access to the DELETE, GET, PATCH and PUT requests for a given ID.
    """
    queryset = Person.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer
    lookup_field = "id"


class ItemEditView(generics.UpdateAPIView):
    # TODO: update docstring
    """Provides access to the PATCH and PUT requests for a given ID.
    """
    permission_classes = (IsAdminUser,)
    queryset = Person.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer
    lookup_field = "id"


class ItemDeleteView(generics.DestroyAPIView):
    # TODO: update docstring
    """Provides access to the DELETE requests for a given ID.
    """
    permission_classes = (IsAdminUser,)
    queryset = Person.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer
    lookup_field = "id"


class ListView(generics.ListAPIView):
    # TODO: update docstring
    """Provides access to the GET request for a list of all Person objects.
    """
    queryset = Person.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer


class CreateView(generics.CreateAPIView):
    # TODO: update docstring
    """Provides access to the POST request for creating Person objects.
    """
    permission_classes = (IsAdminUser,)
    queryset = Person.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer

    def create(self, request, *args, **kwargs):  # pylint: disable=unused-argument
        # TODO: update docstring
        """create
        """
        name_prefix = ""

        if 'name_prefix' in request.data:
            name_prefix = request.data['name_prefix']

        name_first = request.data['name_first']

        name_middle = ""
        if 'name_middle' in request.data:
            name_middle = request.data['name_middle']

        name_last = request.data['name_last']

        name_suffix = ""
        if 'name_suffix' in request.data:
            name_suffix = request.data['name_suffix']

        name = concat_name(name_prefix,
                           name_last,
                           name_first,
                           name_middle,
                           name_suffix)
        request.data['name'] = name

        item_id = slugify(name)

        queryset = Person.objects.filter(  # pylint: disable=no-member
            id=item_id)

        if queryset.count() != 0:
            detail = 'A Person entry already exists with the id '+item_id
            raise serializers.ValidationError(detail)

        return super().create(request, *args, **kwargs)


class PersonHistoryView(generics.RetrieveAPIView):
    # TODO: update docstring
    """Get person history by name
    """
    serializer_class = HistorySerializer
    queryset = Contributor.objects.all()  # pylint: disable=no-member
    lookup_field = "id"
