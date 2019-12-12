#!/usr/bin/python
"""
Defines the DieRoll model
"""
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from rest_framework import serializers
from api.models.die_roll import DieRoll

class Serializer(serializers.ModelSerializer):

    class Meta:
        model = DieRoll
        fields = ('__all__')
