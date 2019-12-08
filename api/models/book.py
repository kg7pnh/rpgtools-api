# -*- coding: utf-8 -*-
"""
Defines the Book model
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
from .base import Base
from .book_format import BookFormat
from .book_format import Serializer as BookFormatSerializer
from .game import Game
from .game import Serializer as GameSerializer
from .contributor import Contributor
from .contributor import Serializer as ContributorSerializer
from .publisher import Publisher
from .publisher import Serializer as PublisherSerializer

VALIDATE_ISBN_10 = RegexValidator(r'^(?:ISBN(?:10)?(?:\-10)?\x20)?[0-9]{9}(\d|X)$',
                                  'Only ISNB-10 formatted strings are allowd.')
VALIDATE_ISBN_13 = RegexValidator(r'^(?:ISBN(?:13)?(?:\-13)?\x20)?:?97(?:8|9)[0-9]{10}$',
                                  'Only ISNB-13 formatted strings are allowd.')

# Create your models here.
class Book(Base):
    """
    Definition for Book
    """
    # Relationships
    book_format = models.ForeignKey(BookFormat,
                                    on_delete=models.PROTECT,
                                    null=True,
                                    blank=True)
    game = models.ManyToManyField(Game,
                                  blank=True,
                                  verbose_name='Game(s)')
    publisher = models.ForeignKey(Publisher,
                                  on_delete=models.PROTECT,
                                  null=True,
                                  blank=True,
                                  verbose_name='Publisher')
    art_assistant = models.ManyToManyField(Contributor,
                                           blank=True,
                                           verbose_name='Art Assistant(s)',
                                           related_name='art_assistant')
    art_director = models.ManyToManyField(Contributor,
                                          blank=True,
                                          verbose_name='Art Director(s)',
                                          related_name='art_director')
    artist_cover = models.ManyToManyField(Contributor,
                                          blank=True,
                                          verbose_name='Cover Artist(s)',
                                          related_name='artist_cover')
    artist_interior = models.ManyToManyField(Contributor,
                                             blank=True,
                                             verbose_name='Interior Artist(s)',
                                             related_name='artist_interior')
    author = models.ManyToManyField(Contributor,
                                    blank=True,
                                    verbose_name='Author(s)',
                                    related_name='author')
    designer = models.ManyToManyField(Contributor,
                                      blank=True,
                                      verbose_name='Designer(s)',
                                      related_name='designer')
    developer = models.ManyToManyField(Contributor,
                                       blank=True,
                                       verbose_name='Developer(s)',
                                       related_name='developer')
    editor = models.ManyToManyField(Contributor,
                                    blank=True,
                                    verbose_name='Editor(s)',
                                    related_name='editor')
    graphic_designer = models.ManyToManyField(Contributor,
                                              blank=True,
                                              verbose_name='Graphic Designer(s)',
                                              related_name='graphic_designer')
    play_tester = models.ManyToManyField(Contributor,
                                         blank=True,
                                         verbose_name='Play Tester(s)',
                                         related_name='play_tester')
    proofreader = models.ManyToManyField(Contributor,
                                         blank=True,
                                         verbose_name='Proofreader(s)',
                                         related_name='proofreader')
    research_assistant = models.ManyToManyField(Contributor,
                                                blank=True,
                                                verbose_name='Research Assistant(s)',
                                                related_name='research_assistant')
    text_manager = models.ManyToManyField(Contributor,
                                          blank=True,
                                          verbose_name='Text Manager(s)',
                                          related_name='text_manager')
    text_processor = models.ManyToManyField(Contributor,
                                            blank=True,
                                            verbose_name='Text Processor(s)',
                                            related_name='text_processor')
    type_setter = models.ManyToManyField(Contributor,
                                         blank=True,
                                         verbose_name='Type Setter(s)',
                                         related_name='type_setter')

    # Attributes
    short_name = models.CharField(max_length=128,
                                  verbose_name='Short Name',
                                  null=True,
                                  blank=True)
    abbreviation = models.CharField(max_length=8,
                                    verbose_name='Abbreviation',
                                    null=True,
                                    blank=True)
    catalog_number = models.CharField(max_length=20,
                                      verbose_name='Catalog Number',
                                      null=True,
                                      blank=True)
    pages = models.IntegerField(verbose_name='Pages',
                                null=True,
                                blank=True)
    publication_year = models.IntegerField(verbose_name='Publication Year',
                                           null=True,
                                           blank=True)
    isbn_10 = models.CharField(max_length=18,
                               verbose_name='ISBN-10',
                               validators=[VALIDATE_ISBN_10],
                               null=True,
                               blank=True)
    isbn_13 = models.CharField(max_length=21,
                               verbose_name='ISBN-13',
                               validators=[VALIDATE_ISBN_13],
                               null=True,
                               blank=True)

    # Manager

    # Functions

    # Meta
    class Meta: # pylint: disable=too-few-public-methods
        """
        Model meta data
        """
        db_table = 'book'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ('name', )

@receiver(pre_save, sender=Book)
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
        model = Book
        fields = ('__all__')

class HyperLinkedSerializer(serializers.HyperlinkedModelSerializer):
    '''
    HyperLinkedSerializer class
    '''
    
    art_assistant = ContributorSerializer(many=True, read_only=True)
    art_director = ContributorSerializer(many=True, read_only=True)
    artist_cover = ContributorSerializer(many=True, read_only=True)
    artist_interior = ContributorSerializer(many=True, read_only=True)
    author = ContributorSerializer(many=True, read_only=True)
    designer = ContributorSerializer(many=True, read_only=True)
    developer = ContributorSerializer(many=True, read_only=True)
    editor = ContributorSerializer(many=True, read_only=True)
    graphic_designer = ContributorSerializer(many=True, read_only=True)
    play_tester = ContributorSerializer(many=True, read_only=True)
    proofreader = ContributorSerializer(many=True, read_only=True)
    research_assistant = ContributorSerializer(many=True, read_only=True)
    text_manager = ContributorSerializer(many=True, read_only=True)
    text_processor = ContributorSerializer(many=True, read_only=True)
    type_setter = ContributorSerializer(many=True, read_only=True)
    book_format = BookFormatSerializer(many=False, read_only=True)
    game = GameSerializer(many=False, read_only=True)
    publisher = PublisherSerializer(many=False, read_only=True)

    class Meta: # pylint: disable=too-few-public-methods
        """
        Class meta data
        """
        model = Book
        fields = ('__all__')

# class BookHistorySerializer(serializers.ModelSerializer):
#     """
#     Book history serializer
#     """

#     class Meta:
#         model = Book.history.model
#         fields = ('__all__')

class BookHistorySerializer(serializers.Serializer):
    """
    Book history serializer
    """
    # history_user = serializers.ReadOnlyField(source='history_user.username')
    changes = serializers.SerializerMethodField()

    def get_changes(self, obj):
        history = obj.history.all()
        changes = []
        for record in obj.history.all():
            print(type(record))
            _change = {
                "type": record.get_history_type_display(),
                "changes": []
            }
            if _change["type"] == "Created":
                # print(record.history_object._meta.get_fields())
                print(record)
                for field in record.history_object._meta.get_fields():
                    # if not isinstance(field, ManyToOneRel) and not isinstance(field, ForeignKey):
                    if not isinstance(field, ManyToOneRel) and not isinstance(field, ManyToManyRel) and not field.primary_key and field.editable and not field.blank:
                        print(field)
                        print(type(field))
                        print(field.name)
                        value = getattr(record.history_object, field.name)
                        print(value)
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
                print("not create record")
                delta = record.diff_against(record.prev_record)
                _change["changes"].extend(
                    [change.__dict__ for change in delta.changes])
            changes.append(_change)
        return changes
