# -*- coding: utf-8 -*-
# TODO: update docstring
"""_summary_
"""
# from django.contrib.postgres.fields import JSONField
from uuid import uuid4
from django.db import models


class ActionRunner(models.Model):
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
    action_input = models.TextField(verbose_name='Input')
    additional_input = models.TextField(verbose_name='Additional Input',
                                        blank=True,
                                        null=True)

    # Manager

    class Meta:  # pylint: disable=too-few-public-methods
        # TODO: update docstring
        """_summary_
        """
        managed = False
