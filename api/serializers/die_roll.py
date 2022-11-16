#!/usr/bin/python
# TODO: update docstring
"""_summary_
"""
# from django.core.validators import MaxValueValidator
# from django.core.validators import MinValueValidator
# from django.db import models
from rest_framework import serializers
from api.models.die_roll import DieRoll


class Serializer(serializers.ModelSerializer):
    # TODO: update docstring
    """_summary_

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        model = DieRoll
        fields = ('__all__')
