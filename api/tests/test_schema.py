# -*- coding: utf-8 -*-
"""
Defines test case run against the API for Schema model
"""
from django.test import tag
from api.tests.base import RPGToolsApiBaseTestCase
from api.tests.base import ADMIN_USER
from api.tests.base import BASE_URL
from api.tests.base import CODES
from api.tests.base import READ_ONLY_USER
from api.tests.base import TOKEN_URL

MODEL_URL = BASE_URL + 'schemas'
POST_URL = MODEL_URL + '/'
EDIT_URL = POST_URL + 'edit/'
DELETE_URL = POST_URL + 'delete/'

INSTANCE_ID = 'attribute-generation-t2000-1e-output-schema'
VERSION = 1
GET_COUNT = 6

FIXTURES = ['test_users',
            'test_schema.json']

CREATE_TEST_VALUE = 'test-schema'
TEST_VALUE = 'UPDATED VIA TESTS'

# REQUEST_DATA_CREATE = {
#     "name": "Test Schema",
#     "description": "A Test Schema",
#     "read_me": "Test Schema==---A test schema.",
#     "url": "https://rpggeek.com/rpg/511/rifts",
#     "abbreviation": "TP"
# }

REQUEST_DATA_CREATE = {
    "name": "Test Schema"
}

REQUEST_DATA_CREATE_DUPLICATE = {
    "name": "Attribute Generation - T2000 1E - Output Schema",
    "description": None,
    "read_me": "",
    "url": None,
    "form_schema": None,
    "schema_type": "Output",
    "document": {},
    "specification": "Draft-07",
    "enabled": True,
    "deprecated": False
}

REQUEST_DATA_PATCH = {
    "description": TEST_VALUE,
}

REQUEST_DATA_PUT = {
    "name": "Attribute Generation - T2000 1E - Output Schema",
    "description": TEST_VALUE,
    "read_me": "",
    "url": None,
    "form_schema": None,
    "schema_type": "Output",
    "document": {},
    "specification": "Draft-07",
    "enabled": True,
    "deprecated": False
}

@tag("schema_admin")
class TestAdmin(RPGToolsApiBaseTestCase):
    """
    Defines schema test case class
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
        self.assertEqual(len(response.json()), GET_COUNT)
        self.assertEqual(response.status_code, CODES["success"])

    def test_get_item_id(self):
        """
        Submits a GET request against POST_URL + INSTANCE_ID + '/' + str(VERSION)
        """
        response = self.rpgtools_api_client.get(POST_URL + INSTANCE_ID + '/' + str(VERSION),
                                                HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.json()['id'], INSTANCE_ID)
        self.assertEqual(response.status_code, CODES["success"])

    def test_get_item_id_history(self):
        """
        Submits a GET request against POST_URL + INSTANCE_ID + '/' + str(VERSION) + '/history'
        """
        response = self.rpgtools_api_client.get(POST_URL + INSTANCE_ID +
                                                '/' + str(VERSION) + '/history',
                                                HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertTrue(response.json())
        self.assertEqual(response.status_code, CODES["success"])

    def test_post_item(self):
        """
        Submits a POST request against POST_URL
        """
        response = self.rpgtools_api_client.post(POST_URL,
                                                 REQUEST_DATA_CREATE,
                                                 format="json",
                                                 HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.json()['id'], CREATE_TEST_VALUE)
        self.assertEqual(response.status_code, CODES["created"])

    def test_post_duplicate_item(self):
        """
        Submits a POST request against POST_URL
        Attemptes to create a duplicate instance
        """
        response = self.rpgtools_api_client.post(POST_URL,
                                                 REQUEST_DATA_CREATE_DUPLICATE,
                                                 format="json",
                                                 HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.json()['version'], VERSION + 1)
        self.assertEqual(response.status_code, CODES["created"])

        response = self.rpgtools_api_client.post(POST_URL,
                                                 REQUEST_DATA_CREATE_DUPLICATE,
                                                 format="json",
                                                 HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.json()['version'], VERSION + 2)
        self.assertEqual(response.status_code, CODES["created"])


    def test_patch_item(self):
        """
        Submits a PATCH request against EDIT_URL + INSTANCE_ID + '/' + str(VERSION)
        """
        response = self.rpgtools_api_client.patch(EDIT_URL + INSTANCE_ID + '/' + str(VERSION),
                                                  REQUEST_DATA_PATCH,
                                                  format="json",
                                                  HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.json()['description'], TEST_VALUE)
        self.assertEqual(response.status_code, CODES["success"])

    def test_put_item(self):
        """
        Submits a PUT request against EDIT_URL + INSTANCE_ID + '/' + str(VERSION)
        """
        response = self.rpgtools_api_client.put(EDIT_URL + INSTANCE_ID + '/' + str(VERSION),
                                                REQUEST_DATA_PUT,
                                                format="json",
                                                HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.json()['description'], TEST_VALUE)
        self.assertEqual(response.status_code, CODES["success"])

    def test_delete_item(self):
        """
        Submits a DELETE request against DELETE_URL + INSTANCE_ID + '/' + str(VERSION)
        """
        response = self.rpgtools_api_client.delete(DELETE_URL + INSTANCE_ID + '/' + str(VERSION),
                                                   HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["deleted"])

@tag("schema_readonly")
class TestReadOnly(RPGToolsApiBaseTestCase):
    """
    Defines schema test case class
    """
    fixtures = FIXTURES
    token = RPGToolsApiBaseTestCase.rpgtools_api_client.post(TOKEN_URL,
                                                             READ_ONLY_USER,
                                                             format="json").json()["access"]

    # read-only user operations
    def test_get_item(self):
        """
        Submits a GET request against POST_URL
        Uses read-only creds
        """
        response = self.rpgtools_api_client.get(MODEL_URL,
                                                HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(len(response.json()), GET_COUNT)
        self.assertEqual(response.status_code, CODES["success"])

    def test_get_item_id(self):
        """
        Submits a GET request against POST_URL + INSTANCE_ID + '/' + str(VERSION)
        Uses read-only creds
        """
        response = self.rpgtools_api_client.get(POST_URL + INSTANCE_ID + '/' + str(VERSION),
                                                HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.json()['id'], INSTANCE_ID)
        self.assertEqual(response.status_code, CODES["success"])

    def test_get_item_id_history(self):
        """
        Submits a GET request against POST_URL + INSTANCE_ID + '/' + str(VERSION) + '/history'
        Uses read-only creds
        """
        response = self.rpgtools_api_client.get(POST_URL + INSTANCE_ID +
                                                '/' + str(VERSION) + '/history',
                                                HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertTrue(response.json())
        self.assertEqual(response.status_code, CODES["success"])

    def test_post_item(self):
        """
        Submits a POST request against POST_URL
        Uses read-only creds
        """
        response = self.rpgtools_api_client.post(POST_URL,
                                                 REQUEST_DATA_CREATE,
                                                 format="json",
                                                 HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["no_permission"])

    def test_patch_item(self):
        """
        Submits a PATCH request against EDIT_URL + INSTANCE_ID + '/' + str(VERSION)
        Uses read-only creds
        """
        response = self.rpgtools_api_client.patch(EDIT_URL + INSTANCE_ID + '/' + str(VERSION),
                                                  REQUEST_DATA_PATCH,
                                                  format="json",
                                                  HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["no_permission"])

    def test_put_item(self):
        """
        Submits a PUT request against EDIT_URL + INSTANCE_ID + '/' + str(VERSION)
        USES read-only creds
        """
        response = self.rpgtools_api_client.put(EDIT_URL + INSTANCE_ID + '/' + str(VERSION),
                                                REQUEST_DATA_PUT,
                                                format="json",
                                                HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["no_permission"])

    def test_delete_item(self):
        """
        Submits a DELETE request against DELETE_URL + INSTANCE_ID + '/' + str(VERSION)
        Uses read-only creds
        """
        response = self.rpgtools_api_client.delete(DELETE_URL + INSTANCE_ID + '/' + str(VERSION),
                                                   HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["no_permission"])

@tag("schema_anonymous")
class TestAnonymous(RPGToolsApiBaseTestCase):
    """
    Defines schema test case class
    """
    fixtures = FIXTURES

    # anonymous user operations
    def test_get_item(self):
        """
        Submits a GET request against POST_URL
        Uses anonymouse access
        """
        response = self.rpgtools_api_client.get(MODEL_URL)
        self.assertEqual(len(response.json()), GET_COUNT)
        self.assertEqual(response.status_code, CODES["success"])

    def test_get_item_id(self):
        """
        Submits a GET request against POST_URL + INSTANCE_ID + '/' + str(VERSION)
        Uses anonymouse access
        """
        response = self.rpgtools_api_client.get(POST_URL + INSTANCE_ID + '/' + str(VERSION))
        self.assertEqual(response.json()['id'], INSTANCE_ID)
        self.assertEqual(response.status_code, CODES["success"])

    def test_get_item_id_history(self):
        """
        Submits a GET request against POST_URL + INSTANCE_ID + '/' + str(VERSION) + '/history'
        Uses anonymouse access
        """
        response = self.rpgtools_api_client.get(POST_URL + INSTANCE_ID +
                                                '/' + str(VERSION) + '/history')
        self.assertTrue(response.json())
        self.assertEqual(response.status_code, CODES["success"])

    def test_post_item(self):
        """
        Submits a POST request against POST_URL
        Uses anonymouse access
        """
        response = self.rpgtools_api_client.post(POST_URL,
                                                 REQUEST_DATA_CREATE,
                                                 format="json")
        self.assertEqual(response.status_code, CODES["no_creds"])

    def test_patch_item(self):
        """
        Submits a PATCH request against EDIT_URL + INSTANCE_ID + '/' + str(VERSION)
        Uses anonymouse access
        """
        response = self.rpgtools_api_client.patch(EDIT_URL + INSTANCE_ID + '/' + str(VERSION),
                                                  REQUEST_DATA_PATCH,
                                                  format="json")
        self.assertEqual(response.status_code, CODES["no_creds"])

    def test_put_item(self):
        """
        Submits a PUT request against EDIT_URL + INSTANCE_ID + '/' + str(VERSION)
        Uses anonymouse access
        """
        response = self.rpgtools_api_client.put(EDIT_URL + INSTANCE_ID + '/' + str(VERSION),
                                                REQUEST_DATA_PUT,
                                                format="json")
        self.assertEqual(response.status_code, CODES["no_creds"])

    def test_delete_item(self):
        """
        Submits a DELETE request against DELETE_URL + INSTANCE_ID + '/' + str(VERSION)
        Uses anonymouse access
        """
        response = self.rpgtools_api_client.delete(DELETE_URL + INSTANCE_ID + '/' + str(VERSION))
        self.assertEqual(response.status_code, CODES["no_creds"])

    def test_get_schema_json(self):
        """
        Submits a GET request against POST_URL + INSTANCE_ID + '/' + str(VERSION) + '.json
        """
        response = self.rpgtools_api_client.get(POST_URL + INSTANCE_ID +
                                                '/' + str(VERSION) + '.json')
        self.assertTrue(response.json()['$id'])
        self.assertEqual(response.status_code, CODES["success"])