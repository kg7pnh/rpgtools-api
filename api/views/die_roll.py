# -*- coding: utf-8 -*-
"""
Defines the DieRoll. views
"""
import api.handlers.die_roll
from api.models.die_roll import DieRoll
from api.models.die_roll import Serializer
from rest_framework import exceptions
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from random import randint

class DieRollRequest(CreateAPIView):
    """
    DieRollRequest
    """
    queryset = DieRoll.objects.all()
    serializer_class = Serializer

    def post(self, request, *args, **kwargs):
        """
        post
        """
        input_data = Serializer(data=request.data,)
        input_data.is_valid(raise_exception=True)

        value = api.handlers.die_roll.run(input_data.data)        

        return Response({"Roll": value},status=status.HTTP_201_CREATED)
