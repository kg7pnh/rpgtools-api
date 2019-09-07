#!/usr/bin/python
"""
Defines the DieRoll model
"""
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from rest_framework import serializers

CONDITION_TYPE = {
    ('==','=='),
    ('<=','<='),
    ('>=','>='),
    ('>','>'),
    ('<','<'),
}

MODIFIER_TYPE = {
    ('+','+'),
    ('-','-'),
    ('*','×'),
    ('/','÷')
}

class DieRoll(models.Model):
    """
    Definition for DieRoll
    """
    # Attributes
    die_size = models.PositiveIntegerField()
    die_count = models.PositiveIntegerField()
    per_modifier_type = models.CharField(max_length=1,
                                         choices=MODIFIER_TYPE,
                                         default='+',
                                         null=True,
                                         blank=True)
    per_modifier_value = models.PositiveIntegerField(default=0,
                                                     null=True,
                                                     blank=True)
    roll_modifier_type = models.CharField(max_length=1,
                                          choices=MODIFIER_TYPE,
                                          default='+',
                                          null=True,
                                          blank=True)
    roll_modifier_value = models.PositiveIntegerField(default=0,
                                                      null=True,
                                                      blank=True)
    post_modifier_type = models.CharField(max_length=1,
                                          choices=MODIFIER_TYPE,
                                          default='+',
                                          null=True,
                                          blank=True)
    post_modifier_value = models.PositiveIntegerField(default=0,
                                                      null=True,
                                                      blank=True)
    reroll_condition = models.CharField(max_length=1,
                                        choices=CONDITION_TYPE,
                                        default='==',
                                        null=True,
                                        blank=True)
    reroll_value = models.IntegerField(default=0,
                                       null=True,
                                       blank=True)

    # Manager

    class Meta:
        managed = False

class Serializer(serializers.ModelSerializer):

    class Meta:
        model = DieRoll
        fields = ('__all__')
