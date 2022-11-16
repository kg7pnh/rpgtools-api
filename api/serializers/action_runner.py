#!/usr/bin/python
# TODO: update docstring
"""_summary_
"""
# from django.contrib.postgres.fields import JSONField
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from rest_framework import serializers
from api.models.action_runner import ActionRunner


class Serializer(serializers.ModelSerializer):
    # TODO: update docstring
    """_summary_

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        # TODO: update docstring
        """_summary_
        """
        model = ActionRunner
        fields = ('__all__')
