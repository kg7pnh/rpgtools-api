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
    Excpects a JSON package in the following format:

        {
            "die_size": 0,
            "die_count": 0,
            "per_modifier": {
                "value": 0,
                "type": "+"
            },
            "roll_modifier": {
                "value": 0,
                "type": "+"
            },
            "post_modifier": {
                "value": 0,
                "type": "+"
            },
            "reroll": {
                "value": 0,
                "condition": "=="
            }
        }
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

        return Response({"roll": value}, status=status.HTTP_201_CREATED)
