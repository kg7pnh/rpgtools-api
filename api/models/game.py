# -*- coding: utf-8 -*-
"""
Defines the Game System model
"""
from django.db import models
from django.db.models import ManyToManyRel
from django.db.models import ManyToOneRel
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from rest_framework import serializers
from .base import Base
from .game_system import GameSystem
from .game_system import Serializer as GameSystemSerializer
from .publisher import Publisher
from .publisher import Serializer as PublisherSerializer

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

    # Manager

    # Functions

    # Meta
    class Meta: # pylint: disable=too-few-public-methods
        """
        Model meta data
        """
        db_table = 'game'
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
        ordering = ('name', )

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

class HyperLinkedSerializer(serializers.HyperlinkedModelSerializer):
    '''
    HyperLinkedSerializer class
    '''
    
    game_system = GameSystemSerializer(many=False, read_only=True)
    publisher = PublisherSerializer(many=False, read_only=True)

    class Meta: # pylint: disable=too-few-public-methods
        """
        Class meta data
        """
        model = GameSystem
        fields = ('__all__')

class GameHistorySerializer(serializers.Serializer):
    """
    Book history serializer
    """
  
    # history_user = serializers.ReadOnlyField(source='history_user.username')
    changes = serializers.SerializerMethodField()

    def get_changes(self, obj):
        history = obj.history.all()
        changes = []
        for record in obj.history.all():
            _change = {
                "type": record.get_history_type_display(),
                "changes": []
            }
            if _change["type"] == "Created":
                for field in record.history_object._meta.get_fields():
                    # if not isinstance(field, ManyToOneRel) and not isinstance(field, ForeignKey):
                    # if not isinstance(field, ManyToOneRel) and not field.primary_key and field.editable and not field.blank:
                    if not isinstance(field, ManyToOneRel) and not isinstance(field, ManyToManyRel) and not field.primary_key and field.editable and not field.blank:
                        value = getattr(record.history_object, field.name)
                        _change["changes"].append({
                            "old": None,
                            "new": value,
                            "type": field.__class__.__name__,
                            "field": field.name
                        })
                    # elif isinstance(field, ForeignKey):
                    #     related_objs = getattr(
                    #         record.history_object, field.name)
                    #     _change["changes"].append({
                    #         "old": None,
                    #         "len": len(related_objs),
                    #         "type": field.__class__.__name__,
                    #         "field": field.name
                    #     })

            else:
                delta = record.diff_against(record.prev_record)
                _change["changes"].extend(
                    [change.__dict__ for change in delta.changes])
            changes.append(_change)
        return changes
