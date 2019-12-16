# -*- coding: utf-8 -*-
"""
Defines test case run against the API for the Contributor model
"""
from django.test import tag
from api.tests.base import RPGToolsApiBaseTestCase
from api.tests.base import ADMIN_USER
from api.tests.base import BASE_URL
from api.tests.base import CODES
from api.tests.base import READ_ONLY_USER
from api.tests.base import TOKEN_URL

MODEL_URL = BASE_URL + 'contributors'
POST_URL = MODEL_URL + '/'
EDIT_URL = POST_URL + 'edit/'
DELETE_URL = POST_URL + 'delete/'

INSTANCE_ID = 'meier-elizabeth'
GET_COUNT = 65

FIXTURES = ['test_users',
    'test_contributor.json']

@tag("contributor_admin")
class TestAdmin(RPGToolsApiBaseTestCase):
    """
    Defines contributor test case class
    """
    fixtures = FIXTURES
    token = RPGToolsApiBaseTestCase.rpgtools_api_client.post(TOKEN_URL,
                                                             ADMIN_USER,
                                                             format="json").json()["access"]

    # admin user operations
    def test_get_item(self):
        """
        Submits a GET request against MODEL_URL
        """
        response = self.rpgtools_api_client.get(MODEL_URL,
                                                HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(len(response.json()),GET_COUNT)
        self.assertEqual(response.status_code, CODES["success"])

    def test_get_item_id(self):
        """
        Submits a GET request against POST_URL + INSTANCE_ID
        """
        response = self.rpgtools_api_client.get(POST_URL + INSTANCE_ID,
                                                HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.json()['id'], INSTANCE_ID)
        self.assertEqual(response.status_code, CODES["success"])

@tag("contributor_anonymous")
class TestAnonymous(RPGToolsApiBaseTestCase):
    """
    Defines contributor test case class
    """
    fixtures = FIXTURES

    # anonymous user operations
    def test_get_item(self):
        """
        Submits a GET request against POST_URL
        Uses anonymouse access
        """
        response = self.rpgtools_api_client.get(MODEL_URL)
        self.assertEqual(len(response.json()),GET_COUNT)
        self.assertEqual(response.status_code, CODES["success"])

    def test_get_item_id(self):
        """
        Submits a GET request against POST_URL + INSTANCE_ID
        Uses anonymouse access
        """
        response = self.rpgtools_api_client.get(POST_URL + INSTANCE_ID)
        self.assertEqual(response.json()['id'], INSTANCE_ID)
        self.assertEqual(response.status_code, CODES["success"])
