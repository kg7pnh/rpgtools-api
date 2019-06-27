# -*- coding: utf-8 -*-
"""
Defines the BookFormat model
"""
from uuid import uuid4
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils import timezone
from rest_framework import serializers
from simple_history.models import HistoricalRecords


FORMAT_TYPE = (
    ('Physical', 'Physical'),
    ('Digital', 'Digital')
)

# Create your models here.
class BookFormat(models.Model):
    """
    Definition for Publisher
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
    name = models.CharField(max_length=256,
                            verbose_name='Name')
    created = models.DateTimeField(editable=False,
                                   verbose_name='Created')
    modified = models.DateTimeField(editable=False,
                                    verbose_name='Modified')
    format_type = models.CharField(max_length=64,
                                   choices=FORMAT_TYPE,
                                   default='Physical',
                                   verbose_name='Type')
    description = models.TextField(verbose_name='Description',
                                   null=True,
                                   blank=True)
    history = HistoricalRecords(excluded_fields=['id', 'modified'])


    # Manager
    book_formats = models.Manager()

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
        self.modified = timezone.now()
        self.id = slugify(self.name) # pylint: disable=invalid-name
        return super().save(*args, **kwargs)

    # Meta
    class Meta: # pylint: disable=too-few-public-methods
        """
        Model meta data
        """
        db_table = 'book_format'
        get_latest_by = 'modified'
        indexes = [models.Index(fields=['id'])]
        ordering = ['id']
        verbose_name = 'Book Format'
        verbose_name_plural = 'Book Formats'

@receiver(pre_save, sender=BookFormat)
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
        model = BookFormat
        fields = ('__all__')
