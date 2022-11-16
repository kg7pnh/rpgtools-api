# -*- coding: utf-8 -*-
# TODO: update docstring
"""_summary_

Returns:
    _type_: _description_
"""
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify
from .contributor import Contributor

# Create your models here.


class Person(Contributor):
    # TODO: update docstring
    """_summary_

    Args:
        Contributor (_type_): _description_

    Returns:
        _type_: _description_
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
    def save(self, *args, **kwargs):  # pylint: disable=arguments-differ
        # TODO: update docstring
        """_summary_

        Returns:
            _type_: _description_
        """
        self.name = concat_name(self.name_prefix,  # pylint: disable=invalid-name
                                self.name_last,
                                self.name_first,
                                self.name_middle,
                                self.name_suffix)

        if not self.id or not self.created:
            self.created = timezone.now()
            self.id = slugify(self.name)  # pylint: disable=invalid-name

        self.modified = timezone.now()
        self.id = slugify(self.name)  # pylint: disable=invalid-name
        return super().save(*args, **kwargs)

    # Meta
    class Meta:  # pylint: disable=too-few-public-methods
        # TODO: update docstring
        """_summary_
        """
        db_table = 'person'
        verbose_name = 'Person'
        verbose_name_plural = 'People'
        ordering = ('name', )


@receiver(pre_save, sender=Person)
def set_fields(sender, instance, **kwargs):  # pylint: disable=unused-argument
    # TODO: update docstring
    """_summary_

    Args:
        sender (_type_): _description_
        instance (_type_): _description_
    """
    instance.name = concat_name(instance.name_prefix,
                                instance.name_last,
                                instance.name_first,
                                instance.name_middle,
                                instance.name_suffix)
    instance.id = slugify(instance.name)


def concat_name(prefix, last, first, middle, suffix):
    # TODO: update docstring
    """_summary_

    Args:
        prefix (_type_): _description_
        last (_type_): _description_
        first (_type_): _description_
        middle (_type_): _description_
        suffix (_type_): _description_

    Returns:
        _type_: _description_
    """
    id_name = last
    if prefix:
        id_name = prefix + " " + id_name
    id_name = id_name + ", " + first
    if middle:
        id_name = id_name + " " + middle
    if suffix:
        id_name = id_name + " " + suffix

    return id_name
