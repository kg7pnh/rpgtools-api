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
class Organization(Contributor):
    """
    Definition for Person
    """
    # Relationships

    # Attributes
    abbreviation = models.CharField(max_length=8,
                                    verbose_name='Abbreviation',
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

        if not self.id or not self.created:
            self.created = timezone.now()
            self.id = slugify(self.name) 
        
        self.modified = timezone.now()
        self.id = slugify(self.name) # pylint: disable=invalid-name
        return super().save(*args, **kwargs)

    # Meta
    class Meta: # pylint: disable=too-few-public-methods
        """
        Model meta data
        """
        db_table = 'organization'
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'
        ordering = ('name', )

@receiver(pre_save, sender=Organization)
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
        model = Organization
        fields = ('__all__')

class OrganizationHistorySerializer(serializers.Serializer):
    """
    Organization history serializer
    """
    # history_user = serializers.ReadOnlyField(source='history_user.username')
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
