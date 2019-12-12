# -*- coding: utf-8 -*-
"""
Defines the BookFormat model
"""
from django.db import models
from django.db.models import ManyToManyRel
from django.db.models import ManyToOneRel
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .base import Base

FORMAT_TYPE = (
    ('Physical', 'Physical'),
    ('Digital', 'Digital')
)

# Create your models here.
class BookFormat(Base):
    """
    Definition for BookFormat
    """
    # Relationships

    # Attributes
    format_type = models.CharField(max_length=64,
                                   choices=FORMAT_TYPE,
                                   default='Physical',
                                   verbose_name='Type')

    # Manager

    # Functions

    # Meta
    class Meta: # pylint: disable=too-few-public-methods
        """
        Model meta data
        """
        db_table = 'book_format'
        verbose_name = 'Book Format'
        verbose_name_plural = 'Book Formats'
        ordering = ('name', )

@receiver(pre_save, sender=BookFormat)
def set_fields(sender, instance, **kwargs): # pylint: disable=unused-argument
    '''
    Set parameter values to html friendly format
    '''
    instance.id = slugify(instance.name)
