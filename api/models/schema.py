# -*- coding: utf-8 -*-
"""
Defines the Schema model
"""
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .base import Base

SCHEMA_SPECIFICATION = (
    ('Draft-07', 'Draft-07'),
)

SCHEMA_TYPE = (
    ('Form', 'Form'),
    ('Object', 'Object'),
    ('Input', 'Input'),
    ('Output', 'Output')
)

class Schema(Base):
    """
    Definition for Schema Model
    """
    # Relationships
    form_schema = models.ForeignKey("self",
                                    blank=True,
                                    null=True,
                                    limit_choices_to={'schema_type': 'Form'},
                                    on_delete=models.PROTECT,
                                    verbose_name='Form Schema')

    # Attributes
    schema_type = models.CharField(choices=SCHEMA_TYPE,
                                   default='Object',
                                   max_length=10,
                                   verbose_name='Schema Type')
    version = models.IntegerField(default=1,
                                  verbose_name='Version')
    document = JSONField(verbose_name='Document',
                         null=True,
                         blank=True)
    specification = models.CharField(max_length=64,
                                     choices=SCHEMA_SPECIFICATION,
                                     default='Draft-07',
                                     verbose_name='Specification')
    enabled = models.BooleanField(default=True,
                                  null=False,
                                  verbose_name='Enabled')
    deprecated = models.BooleanField(default=False,
                                     null=False,
                                     verbose_name='Debricated')

    # Manager

    # Functions

    # Meta
    class Meta: # pylint: disable=too-few-public-methods
        """
        Model meta data
        """
        db_table = 'schema'
        indexes = [models.Index(fields=['id', 'version'])]
        unique_together = ('id', 'version')
        verbose_name = 'Schema'
        verbose_name_plural = 'Schemas'
        ordering = ('name', )

@receiver(pre_save, sender=Schema)
def set_fields(sender, instance, **kwargs): # pylint: disable=unused-argument
    """
    Set parameter values to html friendly format
    """
    instance.id = slugify(instance.name)
