#!/usr/bin/python
"""
Defines the ActionRunner model
"""
from django.contrib.postgres.fields import JSONField
from django.db import models


class ActionRunner(models.Model):
    """
    Definition for ActionRunner
    """
    # Attributes
    action_input = JSONField(verbose_name='Input')

    # Manager

    class Meta: # pylint: disable=too-few-public-methods
        """
        Meta
        """
        managed = False
