# -*- coding: utf-8 -*-
"""
Defines the Workflow model
"""
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from rest_framework import serializers
from .base import Base
from .game import Game
from .action import Action

# Create your models here.
class Workflow(Base):
    """
    Definition for Workflow
    """
    # Relationships
    game = models.ForeignKey(Game,
                             on_delete=models.PROTECT,
                             null=True,
                             blank=True)
    actions = models.ManyToManyField(Action)

    # Attributes

    # Manager

    # Functions

    # Meta
    class Meta: # pylint: disable=too-few-public-methods
        """
        Model meta data
        """
        db_table = 'workflow'
        verbose_name = 'Workflow'
        verbose_name_plural = 'Workflows'

@receiver(pre_save, sender=Workflow)
def set_fields(sender, instance, **kwargs): # pylint: disable=unused-argument
    '''
    Set parameter values to html friendly format
    '''
    instance.id = slugify(instance.name)

class Serializer(serializers.ModelSerializer):
    '''
    Serializer class
    '''
    class Meta: # pylint: disable=too-few-public-methods
        """
        Class meta data
        """
        model = Workflow
        fields = ('__all__')
