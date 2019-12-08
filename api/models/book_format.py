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
from rest_framework import serializers
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

class BookFormatHistorySerializer(serializers.Serializer):
    """
    Book history serializer
    """
    changes = serializers.SerializerMethodField()

    def get_changes(self, obj):
        # for property, value in vars(obj).iteritems():
        #     print(property, ": ", value)
        changes = []
        for record in obj.history.all():
            _change = {
                "type": record.get_history_type_display(),
                "changes": []
            }
            if _change["type"] == "Created":
                for field in record.history_object._meta.get_fields():
                    if not isinstance(field, ManyToOneRel) and not isinstance(field, ManyToManyRel) and not field.primary_key and field.editable and not field.blank:
                        value = getattr(record.history_object, field.name)
                        _change["changes"].append({
                            "old": None,
                            "new": value,
                            "type": field.__class__.__name__,
                            "field": field.name
                        })
            else:
                delta = record.diff_against(record.prev_record)
                _change["changes"].extend(
                    [change.__dict__ for change in delta.changes]
                )
            changes.append(_change)
        return changes