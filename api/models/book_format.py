# -*- coding: utf-8 -*-
# TODO: update docstring
"""_summary_
"""
from django.db import models
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
    # TODO: update docstring
    """_summary_

    Args:
        Base (_type_): _description_
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
    class Meta:  # pylint: disable=too-few-public-methods
        # TODO: update docstring
        """_summary_
        """
        db_table = 'book_format'
        verbose_name = 'Book Format'
        verbose_name_plural = 'Book Formats'
        ordering = ('name', )


@receiver(pre_save, sender=BookFormat)
def set_fields(sender, instance, **kwargs):  # pylint: disable=unused-argument
    # TODO: update docstring
    """_summary_

    Args:
        sender (_type_): _description_
        instance (_type_): _description_
    """
    instance.id = slugify(instance.name)
