# -*- coding: utf-8 -*-
"""
Defines the DieRoll. views
"""
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
import api.handlers.die_roll
from api.models.die_roll import DieRoll
from api.serializers.die_roll import Serializer

class DieRollRequest(CreateAPIView):
    """
    DieRollRequest
    """
    queryset = DieRoll.objects.all() # pylint: disable=no-member
    serializer_class = Serializer

    def post(self, request, *args, **kwargs):
        """
        post
        """
        input_data = Serializer(data=request.data,)
        input_data.is_valid(raise_exception=True)

        value = api.handlers.die_roll.run(input_data.data)

        return Response({"Roll": value}, status=status.HTTP_201_CREATED)
