#!/usr/bin/python
"""
Defines the ActionRunner model
"""
from django.contrib.postgres.fields import JSONField
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from rest_framework import serializers


class ActionRunner(models.Model):
    """
    Definition for ActionRunner
    """
    # Attributes
    action_input = JSONField(verbose_name='Input')

    # Manager
    action_runners = models.Manager()

    class Meta:
        managed = False

class Serializer(serializers.ModelSerializer):

    class Meta:
        model = ActionRunner
        fields = ('__all__')