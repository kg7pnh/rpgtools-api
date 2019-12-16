# -*- coding: utf-8 -*-
"""
Defines the base views
"""
from rest_framework import generics
from rest_framework import schemas
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import renderer_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_swagger.renderers import OpenAPIRenderer
from rest_framework_swagger.renderers import SwaggerUIRenderer

# @api_view()
# @renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
# def schema_view(request):
#     """
#     schema_view
#     """
#     generator = schemas.SchemaGenerator(title='RPGTools API',
#                                         description='API access to tools '+
#                                         'and information for RPG players '+
#                                         'and game masters.')
#     return Response(generator.get_schema(request=request))

class Root(APIView):
    """
    Root
    """
    def get(self, request, *args, **kwargs): # pylint: disable=unused-argument, no-self-use
        """
        get
        """
        return Response({
            "service": "rpg-tools",
            "verion": "1.0.0",
            "description": "API access to tools "+
                           "and information for RPG players "+
                           "and game masters.",
            "swagger_docs": "/api/v1/docs"
        })

class TokenView(TokenObtainPairView):
    """
    TokenView
    """
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        """
        post
        """
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as exception:
            raise InvalidToken(exception.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class CurrentUser(generics.GenericAPIView):
    """
    CurrentUser
    """
    def get(self, request, *args, **kwargs): # pylint: disable=unused-argument
        """
        get
        """
        user = self.request.user
        is_authenticated = user.is_authenticated
        response = {
            "is_authenticated": is_authenticated,
            "username": None,
            "first_name": None,
            "last_name": None,
            "last_login": None,
            "is_superuser": None,
            "thumbnailphoto": None
        }
        if is_authenticated:
            response["username"] = user.username
            response["first_name"] = user.first_name
            response["last_name"] = user.last_name
            response["last_login"] = user.last_login
            response["is_superuser"] = user.is_superuser
        return Response(response)

class IsAdminView(generics.GenericAPIView):
    """
    Is Admin View
    """
    permission_classes = (IsAdminUser,)

    def get(self, request, *args, **kwargs): # pylint: disable=unused-argument, no-self-use
        """
        get
        """
        return Response()
