# -*- coding: utf-8 -*-
"""
Defines the DieRoll. views
"""
import api.actions
from api.models.die_roll import DieRoll
from api.models.die_roll import Serializer
from rest_framework import exceptions
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
        die_roll = Serializer(data=request.data, )
        die_roll.is_valid(raise_exception=True)

        die_size = die_roll.data["die_size"]
        die_count = die_roll.data["die_count"]
        per_modifier_type = die_roll.data["per_modifier_type"]
        per_modifier_value = die_roll.data["per_modifier_value"]
        roll_modifier_type = die_roll.data["roll_modifier_type"]
        roll_modifier_value = die_roll.data["roll_modifier_value"]
        post_modifier_type = die_roll.data["post_modifier_type"]
        post_modifier_value = die_roll.data["post_modifier_value"]
        reroll_condition = die_roll.data["reroll_condition"]
        reroll_value = die_roll.data["reroll_value"]

        value = die_roll.run(data,
                             die_size,
                             die_count,
                             per_modifier_type,
                             per_modifier_value,
                             roll_modifier_type,
                             roll_modifier_value,
                             post_modifier_type,
                             post_modifier_value,
                             reroll_condition,
                             reroll_value)
        

        return Response({"Roll": value},status=200)
