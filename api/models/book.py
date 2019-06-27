# -*- coding: utf-8 -*-
"""
Defines the Book model
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
from .book_format import BookFormat
from .game import Game
from .publisher import Publisher

# Create your models here.
class Book(models.Model):
    """
    Definition for Book
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
    edition_id = models.CharField(max_length=256,
                                  verbose_name='ID',
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
    edition = models.CharField(max_length=256,
                               verbose_name='Edition')
    publisher = models.ForeignKey(Publisher,
                                  on_delete=models.PROTECT,
                                  null=True,
                                  blank=True)
    game = models.ForeignKey(Game,
                             on_delete=models.PROTECT,
                             null=True,
                             blank=True)
    book_format = models.ForeignKey(BookFormat,
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
    history = HistoricalRecords(excluded_fields=['id', 'edition_id', 'modified'])

    # Manager
    books = models.Manager()

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
            self.edition_id = slugify(self.edition)
        self.modified = timezone.now()
        self.id = slugify(self.name) # pylint: disable=invalid-name
        self.edition_id = slugify(self.edition)
        return super().save(*args, **kwargs)

    # Meta
    class Meta: # pylint: disable=too-few-public-methods
        """
        Model meta data
        """
        db_table = 'book'
        get_latest_by = 'modified'
        indexes = [models.Index(fields=['id', 'edition_id'])]
        ordering = ['id', 'edition_id']
        unique_together = ('id', 'edition_id')
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

@receiver(pre_save, sender=Book)
def set_fields(sender, instance, **kwargs): # pylint: disable=unused-argument
    '''
    Set parameter values to html friendly format
    '''
    instance.id = slugify(instance.name)
    instance.edition_id = slugify(instance.edition)

class Serializer(serializers.ModelSerializer):
    '''
    Serializer class
    '''
    def validate(self, validated_data): #pylint: disable=arguments-differ
        game = Book.books.filter(name=validated_data['name'],
                                 version=validated_data['edition']).exists()
        if game:
            raise ValidationError(
                'A book entry with the specified name and edition already exists')
        return validated_data

    class Meta: # pylint: disable=too-few-public-methods
        """
        Class meta data
        """
        model = Book
        fields = ('__all__')
