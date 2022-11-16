# -*- coding: utf-8 -*-
# TODO: update docstring
"""Defines the Workflow views
"""
from django.utils.text import slugify
from rest_framework import generics
from rest_framework import serializers
from rest_framework.permissions import IsAdminUser
from api.models.workflow import Workflow
from api.models.workflow import Serializer
from api.serializers.history import HistorySerializer


class ItemView(generics.RetrieveAPIView):
    # TODO: update docstring
    """Provides access to the DELETE, GET, PATCH and PUT requests for a given ID.
    """
    queryset = Workflow.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer
    lookup_field = "id"


class ItemEditView(generics.UpdateAPIView):
    # TODO: update docstring
    """Provides access to the PATCH and PUT requests for a given ID.
    """
    permission_classes = (IsAdminUser,)
    queryset = Workflow.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer
    lookup_field = "id"


class ItemDeleteView(generics.DestroyAPIView):
    # TODO: update docstring
    """Provides access to the DELETE requests for a given ID.
    """
    permission_classes = (IsAdminUser,)
    queryset = Workflow.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer
    lookup_field = "id"


class ListView(generics.ListAPIView):
    # TODO: update docstring
    """Provides access to the GET request for a list of all Workflow objects.
    """
    queryset = Workflow.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer


class CreateView(generics.CreateAPIView):
    # TODO: update docstring
    """Provides access to the POST request for creating Workflow objects.
    """
    permission_classes = (IsAdminUser,)
    queryset = Workflow.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer

    def create(self, request, *args, **kwargs):  # pylint: disable=unused-argument
        # TODO: update docstring
        """create
        """
        name = request.data['name']
        item_id = slugify(name)

        queryset = Workflow.objects.filter(  # pylint: disable=no-member
            id=item_id)

        if queryset.count() != 0:
            detail = 'A Workflow entry already exists with the id '+item_id
            raise serializers.ValidationError(detail)

        return super().create(request, *args, **kwargs)


class WorkflowHistoryView(generics.RetrieveAPIView):
    # TODO: update docstring
    """Get Workflow history by name
    """
    serializer_class = HistorySerializer
    queryset = Workflow.objects.all()  # pylint: disable=no-member
    lookup_field = "id"
