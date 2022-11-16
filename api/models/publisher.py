# -*- coding: utf-8 -*-
# TODO: update docstring
"""_summary_
"""
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .base import Base

# Create your models here.


class Publisher(Base):
    # TODO: update docstring
    """_summary_

    Args:
        Base (_type_): _description_
    """
    # Relationships

    # Attributes
    abbreviation = models.CharField(max_length=8,
                                    verbose_name='Abbreviation',
                                    null=True,
                                    blank=True)

    # Manager

    # Functions

    # Meta
    class Meta:  # pylint: disable=too-few-public-methods
        # TODO: update docstring
        """_summary_
        """
        db_table = 'publisher'
        verbose_name = 'Publisher'
        verbose_name_plural = 'Publishers'
        ordering = ('name', )


@receiver(pre_save, sender=Publisher)
def set_fields(sender, instance, **kwargs):  # pylint: disable=unused-argument
    # TODO: update docstring
    """_summary_

    Args:
        sender (_type_): _description_
        instance (_type_): _description_
    """
    instance.id = slugify(instance.name)

# class Serializer(serializers.ModelSerializer):
#     """
#     Serializer class
#     """
#     class Meta: # pylint: disable=too-few-public-methods
#         """
#         Class meta data
#         """
#         model = Publisher
#         fields = ('__all__')
