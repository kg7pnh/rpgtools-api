# -*- coding: utf-8 -*-
"""
Defines the Handler model
"""
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from rest_framework import serializers
from .base import Base
from .game import Game

HADNLER_METHODS = FORMAT_TYPE = (
    ('DELETE', 'DELETE'),
    ('GET', 'GET'),
    ('PATCH', 'PATCH'),
    ('POST', 'POST'),
    ('PUT', 'PUT'),
)

# Create your models here.
class Handler(Base):
    """
    Definition for Handler
    """
    # Relationships
    game = models.ForeignKey(Game,
                             on_delete=models.PROTECT)

    # Attributes
    method = models.CharField(max_length=15,
                              choices=HADNLER_METHODS,
                              default='GET',
                              verbose_name='Method')
    api_resource = models.URLField(default='/api/v1/die-roll',
                                   verbose_name='API Resource')

    # Manager

    # Functions

    # Meta
    class Meta: # pylint: disable=too-few-public-methods
        """
        Model meta data
        """
        db_table = 'handler'
        verbose_name = 'Handler'
        verbose_name_plural = 'Handlers'

@receiver(pre_save, sender=Handler)
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
        model = Handler
        fields = ('__all__')
