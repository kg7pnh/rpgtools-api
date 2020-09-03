# -*- coding: utf-8 -*-
"""
Defines the Organization views
"""
from django.utils.text import slugify
from rest_framework import generics
from rest_framework import serializers
from rest_framework.permissions import IsAdminUser
from api.models.contributor import Contributor
from api.models.organization import Organization
from api.serializers.organization import Serializer
from api.serializers.history import HistorySerializer


class ItemView(generics.RetrieveAPIView):  # pylint: disable=too-many-ancestors
    """
    Provides access to the DELETE, GET, PATCH and PUT requests for a given ID.
    """
    queryset = Organization.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer
    lookup_field = "id"


class ItemEditView(generics.UpdateAPIView):  # pylint: disable=too-many-ancestors
    """
    Provides access to the PATCH and PUT requests for a given ID.
    """
    permission_classes = (IsAdminUser,)
    queryset = Organization.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer
    lookup_field = "id"


class ItemDeleteView(generics.DestroyAPIView):  # pylint: disable=too-many-ancestors
    """
    Provides access to the DELETE requests for a given ID.
    """
    permission_classes = (IsAdminUser,)
    queryset = Organization.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer
    lookup_field = "id"


class ListView(generics.ListAPIView):
    """
    Provides access to the GET request for a list of all Organization objects.
    """
    queryset = Organization.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer


class CreateView(generics.CreateAPIView):
    """
    Provides access to the POST request for creating Organization objects.
    """
    permission_classes = (IsAdminUser,)
    queryset = Organization.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer

    def create(self, request, *args, **kwargs):
        """
        create
        """
        item_id = slugify(request.data['name'])

        queryset = Organization.objects.filter(  # pylint: disable=no-member
            id=item_id)

        if queryset.count() != 0:
            detail = 'A Organization entry already exists with the id '+item_id
            raise serializers.ValidationError(detail)

        return super(CreateView, self).create(request, *args, **kwargs)  # pylint: disable=super-with-arguments


class OrganizationHistoryView(generics.RetrieveAPIView):
    """
    Get Organizaiton history by id
    """
    serializer_class = HistorySerializer
    queryset = Contributor.objects.all()  # pylint: disable=no-member
    lookup_field = "id"
