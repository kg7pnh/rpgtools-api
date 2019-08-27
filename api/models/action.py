# -*- coding: utf-8 -*-
"""
Defines the BookFormat model
"""
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from rest_framework import serializers
from .base import Base
from .game import Game
from .handler import Handler
from .schema import Schema

# Create your models here.
class Action(Base):
    """
    Definition for Action
    """
    # Relationships
    game = models.ForeignKey(Game,
                             on_delete=models.PROTECT)
    handler = models.ForeignKey(Handler,
                                on_delete=models.PROTECT)
    input_json = JSONField(default='{"Place": "Holder"}',
                           verbose_name='Input JSON')
    input_schema = models.ForeignKey(Schema,
                                     default='931434e2-9093-4241-bd7a-5d48a2aedc75',
                                     on_delete=models.PROTECT,
                                     related_name='input_schema')
    output_schema = models.ForeignKey(Schema,
                                      default='931434e2-9093-4241-bd7a-5d48a2aedc75',
                                      on_delete=models.PROTECT,
                                      related_name='output_schema')

    # Attributes

    # Manager
    actions = models.Manager()

    # Functions

    # Meta
    class Meta: # pylint: disable=too-few-public-methods
        """
        Model meta data
        """
        db_table = 'action'
        verbose_name = 'Action'
        verbose_name_plural = 'Actions'

@receiver(pre_save, sender=Action)
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
        model = Action
        fields = ('__all__')
