# -*- coding: utf-8 -*-
"""
Defines the base views
"""
from django.conf import settings
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class Root(APIView):
    '''
    Root
    '''
    def get(self, request, *args, **kwargs): # pylint: disable=unused-argument, no-self-use
        '''
        get
        '''
        return Response({
            "service": "rpg-tools",
            "verion": "0.0.1"
        })

class TokenView(TokenObtainPairView):
    '''
    TokenView
    '''
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        '''
        post
        '''
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as exception:
            raise InvalidToken(exception.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class CurrentUser(generics.GenericAPIView):
    '''
    CurrentUser
    '''
    def get(self, request, *args, **kwargs): # pylint: disable=unused-argument
        '''
        get
        '''
        user = self.request.user
        is_authenticated = user.is_authenticated
        response = {
            "is_authenticated": is_authenticated,
            "environment": {
                "omf_environment": settings.OMF_ENVIRONMENT,
                "omf_instance": settings.OMF_INSTANCE
            },
            "username": None,
            "first_name": None,
            "last_name": None,
            "last_login": None,
            "is_superuser": None,
            "thumbnailphoto": None,
            "ldap_groups": [],
            "teams": []
        }
        if is_authenticated:
            response["username"] = user.username
            response["first_name"] = user.first_name
            response["last_name"] = user.last_name
            response["last_login"] = user.last_login
            response["is_superuser"] = user.is_superuser
        return Response(response)
