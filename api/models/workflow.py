# -*- coding: utf-8 -*-
# TODO: update docstring
"""_summary_
"""
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from rest_framework import serializers
from .base import Base
from .game import Game

WORKFLOW_METHOD = (
    ('Manual', 'Manual'),
    ('Automatic', 'Automatic'),
)


class Workflow(Base):
    # TODO: update docstring
    """_summary_

    Args:
        Base (_type_): _description_
    """
    # Relationships
    game = models.ForeignKey(Game,
                             on_delete=models.PROTECT,
                             null=True,
                             blank=True)

    # Attributes
    workflow_method = models.CharField(choices=WORKFLOW_METHOD,
                                       default='Manual',
                                       max_length=15,
                                       verbose_name='Method')
    definition = models.TextField(blank=True,
                                  null=True,
                                  verbose_name='Definition')
    enabled = models.BooleanField(default=True,
                                  null=False,
                                  verbose_name='Enabled')
    deprecated = models.BooleanField(default=False,
                                     null=False,
                                     verbose_name='Deprecated')

    # Manager

    # Functions

    # Meta
    class Meta:  # pylint: disable=too-few-public-methods
        # TODO: update docstring
        """_summary_
        """
        db_table = 'workflow'
        verbose_name = 'Workflow'
        verbose_name_plural = 'Workflows'
        ordering = ('name', )


@receiver(pre_save, sender=Workflow)
def set_fields(instance, **kwargs):  # pylint: disable=unused-argument
    # TODO: update docstring
    """_summary_

    Args:
        sender (_type_): _description_
        instance (_type_): _description_
    """
    instance.id = slugify(instance.name)


class Serializer(serializers.ModelSerializer):
    # TODO: update docstring
    """_summary_

    Args:
        serializers (_type_): _description_
    """
    class Meta:  # pylint: disable=too-few-public-methods
        # TODO: update docstring
        """_summary_
        """
        model = Workflow
        fields = ('__all__')
