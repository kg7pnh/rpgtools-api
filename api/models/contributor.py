# -*- coding: utf-8 -*-
# TODO: update docstring
"""_summary_
"""
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .base import Base

# Create your models here.


class Contributor(Base):
    # TODO: update docstring
    """_summary_

    Args:
        Base (_type_): _description_
    """
    # Meta
    class Meta:  # pylint: disable=too-few-public-methods
        # TODO: update docstring
        """_summary_
        """
        db_table = 'contributor'
        verbose_name = 'Contributor'
        verbose_name_plural = 'Contributors'
        ordering = ['name']


@receiver(pre_save, sender=Contributor)
def set_fields(sender, instance, **kwargs):  # pylint: disable=unused-argument
    # TODO: update docstring
    """_summary_

    Args:
        sender (_type_): _description_
        instance (_type_): _description_
    """
    instance.id = slugify(instance.name)
