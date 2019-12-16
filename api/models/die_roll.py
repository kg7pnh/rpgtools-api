#!/usr/bin/python
"""
Defines the DieRoll model
"""
from django.db import models
from django.contrib.postgres.fields import JSONField

CONDITION_TYPE = {
    ('==', '=='),
    ('<=', '<='),
    ('>=', '>='),
    ('>', '>'),
    ('<', '<'),
}

MODIFIER_TYPE = {
    ('+', '+'),
    ('-', '-'),
    ('*', '×'),
    ('/', '÷')
}

class DieRoll(models.Model):
    """
    Definition for DieRoll
    """
    # Attributes
    die_size = models.PositiveIntegerField(default=0)
    die_count = models.PositiveIntegerField(default=0)
    per_modifier = JSONField(null=True,
                             blank=True)
    roll_modifier = JSONField(null=True,
                             blank=True)
    post_modifier = JSONField(null=True,
                             blank=True)
    reroll = JSONField(null=True,
                       blank=True)

    # Manager

    class Meta: # pylint: disable=too-few-public-methods
        """
        Meta
        """
        managed = False
