# -*- coding: utf-8 -*-
"""
Defines the Game serializers
"""
from django.db import models
from django.db.models import ManyToManyRel
from django.db.models import ManyToOneRel
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from rest_framework import serializers
from api.models.game import Game
from api.serializers.game_system import Serializer as GameSystemSerializer
from api.serializers.publisher import Serializer as PublisherSerializer

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

# class HyperLinkedSerializer(serializers.HyperlinkedModelSerializer):
#     '''
#     HyperLinkedSerializer class
#     '''
    
#     game_system = GameSystemSerializer(many=False, read_only=True)
#     publisher = PublisherSerializer(many=False, read_only=True)

#     class Meta: # pylint: disable=too-few-public-methods
#         """
#         Class meta data
#         """
#         model = Game
#         fields = ('__all__')