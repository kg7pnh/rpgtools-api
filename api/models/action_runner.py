#!/usr/bin/python
"""
Defines the ActionRunner model
"""
# from django.contrib.postgres.fields import JSONField
from django.db import models


class ActionRunner(models.Model):
    """
    Definition for ActionRunner
    """
    # Attributes
    action_input = models.TextField(verbose_name='Input')
    additional_input = models.TextField(verbose_name='Additional Input',
                                        blank=True,
                                        null=True)

    # Manager

    class Meta: # pylint: disable=too-few-public-methods
        """
        Meta
        """
        managed = False
