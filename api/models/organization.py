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


class Organization(Contributor):
    # TODO: update docstring
    """_summary_

    Args:
        Contributor (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Relationships

    # Attributes
    abbreviation = models.CharField(max_length=8,
                                    verbose_name='Abbreviation',
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
        if not self.id or not self.created:
            self.created = timezone.now()
            self.id = slugify(self.name)

        self.modified = timezone.now()
        self.id = slugify(self.name)  # pylint: disable=invalid-name
        return super().save(*args, **kwargs)

    # Meta
    class Meta:  # pylint: disable=too-few-public-methods
        # TODO: update docstring
        """_summary_
        """
        db_table = 'organization'
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'
        ordering = ('name', )


@receiver(pre_save, sender=Organization)
def set_fields(sender, instance, **kwargs):  # pylint: disable=unused-argument
    # TODO: update docstring
    """_summary_

    Args:
        sender (_type_): _description_
        instance (_type_): _description_
    """
    instance.id = slugify(instance.name)
