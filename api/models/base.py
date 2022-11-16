# -*- coding: utf-8 -*-
# TODO: update docstring
"""_summary_

Returns:
    _type_: _description_
"""
from uuid import uuid4
from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from simple_history.models import HistoricalRecords

# Create your models here.


class Base(models.Model):
    # TODO: update docstring
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
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
    created = models.DateTimeField(editable=False,
                                   verbose_name='Created')
    modified = models.DateTimeField(editable=False,
                                    verbose_name='Modified')
    description = models.CharField(max_length=256,
                                   verbose_name='Description',
                                   null=True,
                                   blank=True)
    read_me = models.TextField(verbose_name='Read Me',
                               null=True,
                               blank=True)
    url = models.URLField(verbose_name='Website',
                          null=True,
                          blank=True)
    history = HistoricalRecords(inherit=True)

    # Functions
    def __str__(self):
        # TODO: update docstring
        """_summary_

        Returns:
            _type_: _description_
        """
        return str(self.name)

    def __unicode__(self):
        # TODO: update docstring
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.name

    def save(self, *args, **kwargs):  # pylint: disable=arguments-differ,signature-differs
        # TODO: update docstring
        """_summary_

        Returns:
            _type_: _description_
        """
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
        abstract = True
        get_latest_by = 'modified'
        indexes = [models.Index(fields=['id', 'name'])]
