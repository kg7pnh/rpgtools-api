# -*- coding: utf-8 -*-
# TODO: update docstring
"""_summary_
"""
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.core.validators import RegexValidator
from .base import Base
from .book_format import BookFormat
from .game import Game
from .contributor import Contributor
from .publisher import Publisher

VALIDATE_ISBN_10 = RegexValidator(r'^(?:ISBN(?:10)?(?:\-10)?\x20)?[0-9]{9}(\d|X)$',
                                  'Only ISNB-10 formatted strings are allowd.')
VALIDATE_ISBN_13 = RegexValidator(r'^(?:ISBN(?:13)?(?:\-13)?\x20)?:?97(?:8|9)[0-9]{10}$',
                                  'Only ISNB-13 formatted strings are allowd.')

# Create your models here.


class Book(Base):
    # TODO: update docstring
    """_summary_

    Args:
        Base (_type_): _description_
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
    class Meta:  # pylint: disable=too-few-public-methods
        # TODO: update docstring
        """_summary_
        """
        db_table = 'book'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ('name', )


@receiver(pre_save, sender=Book)
def set_fields(sender, instance, **kwargs):  # pylint: disable=unused-argument
    # TODO: update docstring
    """_summary_

    Args:
        sender (_type_): _description_
        instance (_type_): _description_
    """
    instance.id = slugify(instance.name)
