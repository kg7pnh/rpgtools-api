# -*- coding: utf-8 -*-
# TODO: update docstring
"""Defines the DieRoll. views
"""
import json
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
import api.handlers.die_roll
from api.models.die_roll import DieRoll
from api.serializers.die_roll import Serializer


class DieRollRequest(CreateAPIView):
    # TODO: update docstring
    """DieRollRequest
    Excpects a JSON package in the following format:

        {
            "die_size": 0,
            "die_count": 0,
            "per_modifier": {
                "value": 0,
                "mod_type": "+"
            },
            "roll_modifier": {
                "value": 0,
                "mod_type": "+"
            },
            "post_modifier": {
                "value": 0,
                "mod_type": "+"
            },
            "reroll": {
                "value": 0,
                "condition": "=="
            }
        }
    """
    queryset = DieRoll.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer

    def post(self, request, *args, **kwargs):  # pylint: disable=unused-argument
        # TODO: update docstring
        """post
        """
        input_data = Serializer(data=request.data,)

        value = api.handlers.die_roll.run(
            json.loads(json.dumps(input_data.initial_data)))

        return Response({"roll": value}, status=status.HTTP_201_CREATED)
