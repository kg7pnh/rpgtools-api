# -*- coding: utf-8 -*-
"""
Defines the Schema model
"""
from uuid import uuid4
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.postgres.fields import JSONField
from django.utils import timezone
from markdownx.models import MarkdownxField
from rest_framework import serializers
from simple_history.models import HistoricalRecords

SCHEMA_SPECIFICATION = (
    ('Draft-07', 'Draft-07'),
)

SCHEMA_TYPE = (
    ('Form', 'Form'),
    ('Object', 'Object')
)

class Schema(models.Model):
    """
    Definition for BaseModel
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
    version = models.IntegerField(default=1,
                                  editable=False,
                                  verbose_name='Version')
    created = models.DateTimeField(editable=False,
                                   verbose_name='Created')
    modified = models.DateTimeField(editable=False,
                                    verbose_name='Modified')
    document = JSONField(verbose_name='Data',
                         null=True,
                         blank=True)
    schema_type = models.CharField(max_length=64,
                                   choices=SCHEMA_TYPE,
                                   default='Object',
                                   verbose_name='Type')
    specification = models.CharField(max_length=64,
                                     choices=SCHEMA_SPECIFICATION,
                                     default='Draft-07',
                                     verbose_name='Specification')
    description = models.TextField(verbose_name='Description',
                                   null=True,
                                   blank=True)
    read_me = MarkdownxField(verbose_name='Read Me')
    history = HistoricalRecords(excluded_fields=['id', 'modified', 'version'])

    # Manager
    schemas = models.Manager()

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
        On save, update timestamps and id fields
        '''
        if not self.id or not self.created:
            self.created = timezone.now()
            self.id = slugify(self.name) #pylint: disable=invalid-name
        self.modified = timezone.now()
        self.id = slugify(self.name) #pylint: disable=invalid-name
        return super().save(*args, **kwargs)

    # Meta
    class Meta: # pylint: disable=too-few-public-methods
        """
        Model meta data
        """
        db_table = 'schema'
        get_latest_by = 'modified'
        indexes = [models.Index(fields=['id', 'version'])]
        ordering = ['id']
        unique_together = ('id', 'version')
        verbose_name = 'Schema'
        verbose_name_plural = 'Schemas'

@receiver(pre_save, sender=Schema)
def set_fields(sender, instance, **kwargs): # pylint: disable=unused-argument
    '''
    Set parameter values to html friendly format
    '''
    instance.id = slugify(instance.name)

class Serializer(serializers.ModelSerializer):
    '''
    Serializer class
    '''
    class Meta: #pylint: disable=too-few-public-methods
        """
        Class meta data
        """
        model = Schema
        fields = ('__all__')

class HrefSerializer(serializers.ModelSerializer):
    '''
    HrefSerializer class
    '''
    document = serializers.SerializerMethodField()
    class Meta: #pylint: disable=too-few-public-methods
        """
        Class meta data
        """
        model = Schema
        fields = ('__all__')

    def get_document(self, schema):
        '''
        return document
        '''
        request = self.context['request']
        print(request)
        document = schema.document
        document["$id"] = request.build_absolute_uri(reverse(
            "schema_item_version", kwargs={'id': schema.id, 'version': schema.version}))
        return document

class DocumentSerializer(HrefSerializer):
    '''
    DocumentSerializer class
    '''
    def to_representation(self, schema): #pylint: disable=arguments-differ
        print(schema)
        return self.get_document(schema)
