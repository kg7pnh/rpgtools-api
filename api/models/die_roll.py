#!/usr/bin/python
# TODO: update docstring
"""_summary_
"""
from uuid import uuid4
from django.db import models
# from django.contrib.postgres.fields import JSONField

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
    ('*', 'X'),
    ('*', 'x'),
    ('*', '×'),
    ('/', '÷')
}


class DieRoll(models.Model):
    # TODO: update docstring
    """_summary_

    Args:
        models (_type_): _description_
    """
    # Attributes
    _id = models.UUIDField(primary_key=True,
                           default=uuid4,
                           editable=False,
                           verbose_name='_ID')
    die_size = models.PositiveIntegerField(default=0)
    die_count = models.PositiveIntegerField(default=0)
    per_modifier = models.TextField(null=True,
                                    blank=True)
    roll_modifier = models.TextField(null=True,
                                     blank=True)
    post_modifier = models.TextField(null=True,
                                     blank=True)
    reroll = models.TextField(null=True,
                              blank=True)

    # Manager

    class Meta:  # pylint: disable=too-few-public-methods
        # TODO: update docstring
        """_summary_
        """
        managed = False
