# -*- coding: utf-8 -*-
"""
Defines the DieRoll. views
"""
from api.models.die_roll import DieRoll
from api.models.die_roll import Serializer
from rest_framework import exceptions
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from random import randint

def roll(die_size):
	return randint(1,die_size)

def processModifier(value, modifier, modification):
    if modification == '+':
        value = value + modifier
    if modification == '-':
        value = value - modifier
    if modification == '*':
        value = value * modifier
    if modification == '/':
        value = value / modifier
    return value

def perform_die_roll(die_size,
                      die_count,
                      per_modifier_type,
                      per_modifier_value,
                      roll_modifier_type,
                      roll_modifier_value,
                      post_modifier_type,
                      post_modifier_value):

    count = 1
    die_roll = 0
    result = 0
    while count <= die_count:
        count += 1
        die_roll = roll(die_size)

        # if a per roll modifier is specified, apply it
        if per_modifier_type:
            die_roll = processModifier(die_roll, per_modifier_value, per_modifier_type)

        result = result + die_roll

    # if a roll modifier is specified, apply it
    if roll_modifier_type:
        result = processModifier(result, roll_modifier_value, roll_modifier_type)
    
    # if a post roll modifier is specified, apply it
    if post_modifier_type:
        result = processModifier(result, post_modifier_value, post_modifier_type)
    
    # return the result
    return result


class DieRollRequest(CreateAPIView):
    """
    DieRollRequest
    """
    queryset = DieRoll.die_rolls.all()
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

        return Response({"Roll": perform_die_roll(die_size,
                                                     die_count,
                                                     per_modifier_type,
                                                     per_modifier_value,
                                                     roll_modifier_type,
                                                     roll_modifier_value,
                                                     post_modifier_type,
                                                     post_modifier_value)},status=200)
