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
from .game_system import GameSystem
from .publisher import Publisher

# Create your models here.
class Game(Base):
    """
    Definition for GameSystem
    """
    # Relationships
    game_system = models.ForeignKey(GameSystem,
                                    on_delete=models.PROTECT,
                                    null=True,
                                    blank=True)
    publisher = models.ForeignKey(Publisher,
                                  on_delete=models.PROTECT,
                                  null=True,
                                  blank=True)

    # Attributes
    short_name = models.CharField(max_length=128,
                                  verbose_name='Short Name',
                                  null=True,
                                  blank=True)
    abbreviation = models.CharField(max_length=8,
                                    verbose_name='Abbreviation',
                                    null=True,
                                    blank=True)
    url = models.URLField(verbose_name='Website',
                          null=True,
                          blank=True)


    # Manager
    games = models.Manager()

    # Functions

    # Meta
    class Meta: # pylint: disable=too-few-public-methods
        """
        Model meta data
        """
        db_table = 'game'
        verbose_name = 'Game'
        verbose_name_plural = 'Games'

@receiver(pre_save, sender=GameSystem)
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
        model = Game
        fields = ('__all__')
