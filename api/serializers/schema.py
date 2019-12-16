# -*- coding: utf-8 -*-
"""
Defines the Schema serializers
"""
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models import ManyToManyRel
from django.db.models import ManyToOneRel
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify
from rest_framework import serializers
from api.models.schema import Schema

class Serializer(serializers.ModelSerializer):
    """
    Serializer class
    """
    class Meta: #pylint: disable=too-few-public-methods
        """
        Class meta data
        """
        model = Schema
        fields = ('__all__')

class HrefSerializer(serializers.ModelSerializer):
    """
    HrefSerializer class
    """
    document = serializers.SerializerMethodField()
    class Meta: #pylint: disable=too-few-public-methods
        """
        Class meta data
        """
        model = Schema
        fields = ('__all__')

    def get_document(self, schema):
        """
        return document
        """
        request = self.context['request']
        document = schema.document
        document["$id"] = request.build_absolute_uri(reverse(
            "schema_item_version_json", kwargs={'id': schema.id, 'version': schema.version}))
        return document

class DocumentSerializer(HrefSerializer):
    """
    DocumentSerializer class
    """
    def to_representation(self, schema): #pylint: disable=arguments-differ
        return self.get_document(schema)
