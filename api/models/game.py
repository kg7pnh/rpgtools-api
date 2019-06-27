# -*- coding: utf-8 -*-
"""
Defines the Game model
"""
from uuid import uuid4
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from simple_history.models import HistoricalRecords
from .publisher import Publisher

# Create your models here.
class Game(models.Model):
    """
    Definition for Game
    """
    # Relationships

    # Attributes
    _id = models.UUIDField(primary_key=True,
                           default=uuid4,
                           editable=False,
                           verbose_name='_ID')
    id = models.CharField(max_length=256,
                          verbose_name='ID',
                          editable=False)
    version_id = models.CharField(max_length=16,
                                  verbose_name='Version ID',
                                  editable=False)
    name = models.CharField(max_length=256,
                            verbose_name='Name')
    short_name = models.CharField(max_length=128,
                                  verbose_name='Short Name',
                                  null=True,
                                  blank=True)
    abbreviation = models.CharField(max_length=8,
                                    verbose_name='Abbreviation',
                                    null=True,
                                    blank=True)
    version = models.CharField(max_length=16,
                               verbose_name='Version')
    publisher = models.ForeignKey(Publisher,
                                  on_delete=models.PROTECT,
                                  null=True,
                                  blank=True)
    created = models.DateTimeField(editable=False,
                                   verbose_name='Created')
    modified = models.DateTimeField(editable=False,
                                    verbose_name='Modified')
    description = models.TextField(verbose_name='Description',
                                   null=True,
                                   blank=True)
    history = HistoricalRecords(excluded_fields=['id', 'modified', 'version_id'])


    # Manager
    games = models.Manager()

    # Functions
    def __str__(self):
        '''
        __str__
        '''
        return self.name

    def __unicode__(self):
        '''
        __unicode__
        '''
        return self.name

    def save(self, *args, **kwargs): # pylint: disable=arguments-differ
        '''
        On save, update timestamps and parameters
        '''
        if not self.id or not self.created:
            self.created = timezone.now()
            self.id = slugify(self.name) # pylint: disable=invalid-name
            self.version_id = slugify(self.version) # pylint: disable=invalid-name
        self.modified = timezone.now()
        self.id = slugify(self.name) # pylint: disable=invalid-name
        self.version_id = slugify(self.version) # pylint: disable=invalid-name
        return super().save(*args, **kwargs)

    # Meta
    class Meta: # pylint: disable=too-few-public-methods
        """
        Model meta data
        """
        db_table = 'game'
        get_latest_by = 'modified'
        indexes = [models.Index(fields=['id', 'version_id'])]
        ordering = ['id', 'version_id']
        unique_together = ('id', 'version_id')
        verbose_name = 'Game'
        verbose_name_plural = 'Games'

@receiver(pre_save, sender=Game)
def set_fields(sender, instance, **kwargs): # pylint: disable=unused-argument
    '''
    Set parameter values to html friendly format
    '''
    instance.id = slugify(instance.name)
    instance.version_id = slugify(instance.version)

class Serializer(serializers.ModelSerializer):
    '''
    Serializer class
    '''
    def validate(self, validated_data): #pylint: disable=arguments-differ
        game = Game.games.filter(name=validated_data['name'],
                                 version=validated_data['version']).exists()
        if game:
            raise ValidationError(
                'A game entry with the specified name and version already exists')
        return validated_data

    class Meta: # pylint: disable=too-few-public-methods
        """
        Class meta data
        """
        model = Game
        fields = ('__all__')
