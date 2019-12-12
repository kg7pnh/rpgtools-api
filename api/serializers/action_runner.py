#!/usr/bin/python
"""
Defines the ActionRunner serializers
"""
from django.contrib.postgres.fields import JSONField
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from rest_framework import serializers
from api.models.action_runner import ActionRunner

class Serializer(serializers.ModelSerializer):

    class Meta:
        model = ActionRunner
        fields = ('__all__')