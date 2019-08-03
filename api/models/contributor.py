# -*- coding: utf-8 -*-
"""
Defines the Game System model
"""
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from rest_framework import serializers
from .base import Base

# Create your models here.
class Contributor(Base):
    """
    Definition for Contributor
    """
    # Relationships

    # Attributes

    # Manager
    contributors = models.Manager()

    # Functions

    # Meta
    class Meta: # pylint: disable=too-few-public-methods
        """
        Model meta data
        """
        db_table = 'contributor'
        verbose_name = 'Contributor'
        verbose_name_plural = 'Contributors'
        ordering = ['name']

@receiver(pre_save, sender=Contributor)
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
        model = Contributor
        fields = ('__all__')
