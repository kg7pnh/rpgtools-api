# -*- coding: utf-8 -*-
# TODO: update docstring
"""_summary_
"""
from django.test import TestCase
from django.test.utils import override_settings
from rest_framework.test import APIClient

ADMIN_USER = {
    "username": "admin",
    "password": "adminpass"
}

RO_USER = {
    "username": "read-only",
    "password": "ropassword"
}

API_URL = '/api/v1/'

T_URL = API_URL + 'token'

CODES = {
    "success": 200,
    "created": 201,
    "deleted": 204,
    "found": 302,
    "bad_request": 400,
    "no_creds": 401,
    "no_permission": 403
}


@override_settings(AUTHENTICATION_BACKENDS=('django.contrib.auth.backends.ModelBackend',))
class RpgtApiBTC(TestCase):
    # TODO: update docstring
    """_summary_

    Args:
        TestCase (_type_): _description_
    """
    # http://jmoiron.net/blog/subclassing-djangos-testcase/
    rpgt_api_cli = APIClient()
    rpgtools_api_client_ro = APIClient()
