# -*- coding: utf-8 -*-
"""
Defines the Handler model
"""
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .schema import Schema
from .base import Base

HANDLER_ACTIONS = (
    ('die_roll', 'die_roll'),
    ('addition', 'addition'),
    ('average', 'average'),
)

HADNLER_METHODS = (
    ('DELETE', 'DELETE'),
    ('GET', 'GET'),
    ('PATCH', 'PATCH'),
    ('POST', 'POST'),
    ('PUT', 'PUT'),
)


# Create your models here.
class Handler(Base):
    """
    Definition for Handler
    """
    # Relationships
    input_schema = models.ForeignKey(Schema,
                                     blank=True,
                                     limit_choices_to={'schema_type': 'Input'},
                                     null=True,
                                     on_delete=models.PROTECT,
                                     related_name='handler_input_schema')
    output_schema = models.ForeignKey(Schema,
                                      blank=True,
                                      limit_choices_to={'schema_type': 'Output'},
                                      null=True,
                                      on_delete=models.PROTECT,
                                      related_name='handler_output_schema')

    # Attributes
    method = models.CharField(choices=HADNLER_METHODS,
                              default='POST',
                              max_length=15,
                              verbose_name='Method')
    api_handler = models.CharField(choices=HANDLER_ACTIONS,
<<<<<<< HEAD
<<<<<<< HEAD
                                   default='/api/v1/die-roll',
                                   max_length=150,
                                   verbose_name='API Handler')
=======
                                  default='/api/v1/die-roll',
                                  max_length=150,
                                  verbose_name='API Handler')
>>>>>>> cec4f9a092090d14e97cbb0a46e0a23d701b33f7
=======
                                  default='/api/v1/die-roll',
                                  max_length=150,
                                  verbose_name='API Handler')
>>>>>>> cec4f9a092090d14e97cbb0a46e0a23d701b33f7

    # Manager

    # Functions

    # Meta
    class Meta: # pylint: disable=too-few-public-methods
        """
        Model meta data
        """
        db_table = 'handler'
        verbose_name = 'Handler'
        verbose_name_plural = 'Handlers'
        ordering = ('name', )

@receiver(pre_save, sender=Handler)
def set_fields(sender, instance, **kwargs): # pylint: disable=unused-argument
    '''
    Set parameter values to html friendly format
    '''
    instance.id = slugify(instance.name)
