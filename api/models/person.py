# -*- coding: utf-8 -*-
"""
Defines the Game System model
"""
from django.db import models
from django.db.models import ManyToManyRel
from django.db.models import ManyToOneRel
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify
from rest_framework import serializers
from .contributor import Contributor

# Create your models here.
class Person(Contributor):
    """
    Definition for Person
    """
    # Relationships

    # Attributes
    name_prefix = models.CharField(max_length=6,
                                   verbose_name='Prefix',
                                   null=True,
                                   blank=True)
    name_first = models.CharField(max_length=25,
                                  verbose_name='First Name')
    name_middle = models.CharField(max_length=50,
                                   verbose_name='Middle Name',
                                   null=True,
                                   blank=True)
    name_last = models.CharField(max_length=25,
                                 verbose_name='Last Name')
    name_suffix = models.CharField(max_length=50,
                                   verbose_name='Prefix',
                                   null=True,
                                   blank=True)

    # Manager

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
        self.name = concat_name(self.name_prefix, # pylint: disable=invalid-name
                                self.name_last,
                                self.name_first,
                                self.name_middle,
                                self.name_suffix)

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
        db_table = 'person'
        verbose_name = 'Person'
        verbose_name_plural = 'People'
        ordering = ('name', )

@receiver(pre_save, sender=Person)
def set_fields(sender, instance, **kwargs): # pylint: disable=unused-argument
    '''
    Set parameter values to html friendly format
    '''
    instance.name = concat_name(instance.name_prefix,
                                instance.name_last,
                                instance.name_first,
                                instance.name_middle,
                                instance.name_suffix)
    instance.id = slugify(instance.name)

def concat_name(prefix, last, first, middle, suffix):

    id_name = last
    if prefix:
        id_name = prefix + " " + id_name
    id_name = id_name + ", " + first
    if middle:
        id_name = id_name + " " + middle
    if suffix:
        id_name = id_name + " " + suffix

    return id_name

class Serializer(serializers.ModelSerializer):
    '''
    Serializer class
    '''
    class Meta: # pylint: disable=too-few-public-methods
        """
        Class meta data
        """
        model = Person
        fields = ('__all__')

class PersonHistorySerializer(serializers.Serializer):
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
