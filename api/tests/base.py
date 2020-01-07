# -*- coding: utf-8 -*-
"""
Base module for all tests
"""
from django.test import TestCase
from django.test.utils import override_settings
from rest_framework.test import APIClient

ADMIN_USER = {
    "username": "admin",
    "password": "adminpass"
}

READ_ONLY_USER = {
    "username": "read-only",
    "password": "ropassword"
}

BASE_URL = '/api/v1/'

TOKEN_URL = BASE_URL + 'token'

CODES = {
    "success": 200,
    "created": 201,
    "deleted": 204,
    "bad_request": 400,
    "no_creds": 401,
    "no_permission": 403
}

@override_settings(AUTHENTICATION_BACKENDS=('django.contrib.auth.backends.ModelBackend',))
class RPGToolsApiBaseTestCase(TestCase):
    """
    http://jmoiron.net/blog/subclassing-djangos-testcase/
    """
    rpgtools_api_client = APIClient()
    rpgtools_api_client_ro = APIClient()
