# -*- coding: utf-8 -*-
"""
Defines the user and group serializers
"""
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    '''
    UserSerializer
    '''
    class Meta: # pylint: disable=too-few-public-methods
        '''
        Meta
        '''
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    '''
    GroupSerializer
    '''
    class Meta: # pylint: disable=too-few-public-methods
        '''
        Meta
        '''
        model = Group
        fields = ('url', 'name')
