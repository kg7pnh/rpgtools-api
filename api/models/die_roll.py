#!/usr/bin/python
"""
Defines the DieRoll model
"""
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from rest_framework import serializers

class DieRoll(models.Model):
    """
    Definition for DieRoll
    """
    # Attributes
    die_size = models.PositiveIntegerField(default=6)
    die_count = models.PositiveIntegerField(default=3)
    per_modifier_type = models.CharField(max_length=1,
                                         null=True,
                                         blank=True)
    per_modifier_value = models.PositiveIntegerField(default=0,
                                                     null=True,
                                                     blank=True)
    roll_modifier_type = models.CharField(max_length=1,
                                          null=True,
                                          blank=True)
    roll_modifier_value = models.PositiveIntegerField(default=0,
                                                      null=True,
                                                      blank=True)
    post_modifier_type = models.CharField(max_length=1,
                                          null=True,
                                          blank=True)
    post_modifier_value = models.PositiveIntegerField(default=0,
                                                      null=True,
                                                      blank=True)

    # Manager
    die_rolls = models.Manager()

    class Meta:
        managed = False

class Serializer(serializers.ModelSerializer):

    class Meta:
        model = DieRoll
        fields = ('__all__')

    def validate(self, data):
        if not data.get('die_size'):
            data['die_size'] = 6
        if not data.get('die_count'):
            data['die_count'] = 3
        if not data.get('per_modifier_type'):
            data['per_modifier_type'] = '+'
        if not data.get('per_modifier_value'):
            data['per_modifier_value'] = 0
        if not data.get('roll_modifier_type'):
            data['roll_modifier_type'] = '+'
        if not data.get('roll_modifier_value'):
            data['roll_modifier_value'] = 0
        if not data.get('post_modifier_type'):
            data['post_modifier_type'] = '+'
        if not data.get('post_modifier_value'):
            data['post_modifier_value'] = 0
        return data
