# -*- coding: utf-8 -*-
# TODO: update docstring
"""_summary_
"""
from django.db import models
from django.db.models import ManyToManyRel
from django.db.models import ManyToOneRel
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from rest_framework import serializers
from api.models.game_system import GameSystem
from api.serializers.publisher import Serializer as PublisherSerializer


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
        model = GameSystem
        fields = ('__all__')

# class HyperLinkedSerializer(serializers.HyperlinkedModelSerializer):
#     '''
#     HyperLinkedSerializer class
#     '''

#     publisher = PublisherSerializer(many=False, read_only=True)

#     class Meta: # pylint: disable=too-few-public-methods
#         """
#         Class meta data
#         """
#         model = GameSystem
#         ref_name = 'GameSystemHLS'
#         fields = ('__all__')
