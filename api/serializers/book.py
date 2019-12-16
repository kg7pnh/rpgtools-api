# -*- coding: utf-8 -*-
"""
Defines the Book serializers
"""
from django.db import models
from django.db.models import ManyToManyRel
from django.db.models import ManyToOneRel
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.core.validators import RegexValidator
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from api.models.book import Book
from api.serializers.book_format import Serializer as BookFormatSerializer
from api.serializers.game import Serializer as GameSerializer
from api.serializers.contributor import Serializer as ContributorSerializer
from api.serializers.publisher import Serializer as PublisherSerializer


class Serializer(serializers.ModelSerializer):
    '''
    Serializer class
    '''

    class Meta: # pylint: disable=too-few-public-methods
        """
        Class meta data
        """
        model = Book
        fields = ('__all__')

# class HyperLinkedSerializer(serializers.HyperlinkedModelSerializer):
#     '''
#     HyperLinkedSerializer class
#     '''
#     art_assistant = ContributorSerializer(many=True, read_only=True)
#     art_director = ContributorSerializer(many=True, read_only=True)
#     artist_cover = ContributorSerializer(many=True, read_only=True)
#     artist_interior = ContributorSerializer(many=True, read_only=True)
#     author = ContributorSerializer(many=True, read_only=True)
#     designer = ContributorSerializer(many=True, read_only=True)
#     developer = ContributorSerializer(many=True, read_only=True)
#     editor = ContributorSerializer(many=True, read_only=True)
#     graphic_designer = ContributorSerializer(many=True, read_only=True)
#     play_tester = ContributorSerializer(many=True, read_only=True)
#     proofreader = ContributorSerializer(many=True, read_only=True)
#     research_assistant = ContributorSerializer(many=True, read_only=True)
#     text_manager = ContributorSerializer(many=True, read_only=True)
#     text_processor = ContributorSerializer(many=True, read_only=True)
#     type_setter = ContributorSerializer(many=True, read_only=True)
#     book_format = BookFormatSerializer(many=False, read_only=True)
#     game = GameSerializer(many=False, read_only=True)
#     publisher = PublisherSerializer(many=False, read_only=True)

#     class Meta: # pylint: disable=too-few-public-methods
#         """
#         Class meta data
#         """
#         model = Book
#         ref_name = 'BookHLS'
#         fields = ('__all__')