# -*- coding: utf-8 -*-
# TODO: update docstring
"""Defines the base views
"""
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class Root(APIView):
    # TODO: update docstring
    """Root
    """
    service = "rpg-tools"
    version = "1.0.0"
    description = "API access to tools " + \
        "and information for RPG players " + \
        "and game masters."
    swagger_docs = "/api/v1/swagger/"

    def get(self, request, *args, **kwargs):  # pylint: disable=unused-argument
        # TODO: update docstring
        """get
        """
        return Response({
            "service": self.service,
            "verion": self.version,
            "description": self.description,
            "swagger_docs": self.swagger_docs
        })


class TokenView(TokenObtainPairView):
    # TODO: update docstring
    """TokenView
    """
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):  # pylint: disable=unused-argument
        # TODO: update docstring
        """post
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class CurrentUser(generics.GenericAPIView):
    # TODO: update docstring
    """CurrentUser
    """

    def get(self, request, *args, **kwargs):  # pylint: disable=unused-argument
        # TODO: update docstring
        """get
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
    # TODO: update docstring
    """Is Admin View
    """
    permission_classes = (IsAdminUser,)

    def get(self, request, *args, **kwargs):  # pylint: disable=unused-argument, no-self-use
        # TODO: update docstring
        """get
        """
        return Response()
