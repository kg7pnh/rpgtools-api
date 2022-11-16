# -*- coding: utf-8 -*-
# TODO: break out into individual files under api/tests/book_format
"""
Defines test case run against the API for BookFormat model
"""
from django.test import tag
from api.tests.base import RpgtApiBTC
from api.tests.base import ADMIN_USER
from api.tests.base import API_URL
from api.tests.base import CODES
from api.tests.base import RO_USER
from api.tests.base import T_URL

MODEL_URL = API_URL + 'bookformats'
POST_URL = MODEL_URL + '/'
EDIT_URL = POST_URL + 'edit/'
DELETE_URL = POST_URL + 'delete/'

INSTANCE_ID = 'epub'
GET_COUNT = 7

FIXTURES = ['test_users',
            'test_bookformat.json']

CREATE_TEST_VALUE = 'test-format'
TEST_VALUE = 'UPDATED VIA TESTS'

REQUEST_DATA_CREATE = {
    "name": "Test Format",
    "description": "Test format",
    "read_me": "Test Format==---A test format",
    "url": "https://www.google.com",
    "format_type": "Physical"
}

REQUEST_DATA_CREATE_DUPLICATE = {
    "name": "EPUB",
    "description": "An electronic book format.",
    "read_me": "EPUB==---An electronic book format.",
    "url": "https://en.wikipedia.org/wiki/EPUB",
    "format_type": "Digital"
}

REQUEST_DATA_PATCH = {
    "description": TEST_VALUE,
}

REQUEST_DATA_PUT = {
    "name": "EPUB",
    "description": TEST_VALUE,
    "read_me": "EPUB==---An electronic book format.",
    "url": "https://en.wikipedia.org/wiki/EPUB",
    "format_type": "Digital"
}


@tag("book_format_admin")
class TestAdmin(RpgtApiBTC):
    """
    Defines book_format test case class
    """
    fixtures = FIXTURES
    token = RpgtApiBTC.rpgt_api_cli.post(T_URL,
                                         ADMIN_USER,
                                         format="json").json()["access"]

    # admin user operations
    def test_get_item(self):
        """
        Submits a GET request against MODEL_URL
        """
        response = self.rpgt_api_cli.get(MODEL_URL,
                                         HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(len(response.json()), GET_COUNT)
        self.assertEqual(response.status_code, CODES["success"])

    def test_get_item_id(self):
        """
        Submits a GET request against POST_URL + INSTANCE_ID
        """
        response = self.rpgt_api_cli.get(POST_URL + INSTANCE_ID,
                                         HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.json()['id'], INSTANCE_ID)
        self.assertEqual(response.status_code, CODES["success"])

    def test_get_item_id_history(self):
        """
        Submits a GET request against POST_URL + INSTANCE_ID + '/history'
        """
        response = self.rpgt_api_cli.get(POST_URL + INSTANCE_ID + '/history',
                                         HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertTrue(response.json())
        self.assertEqual(response.status_code, CODES["success"])

    def test_post_item(self):
        """
        Submits a POST request against POST_URL
        """
        response = self.rpgt_api_cli.post(POST_URL,
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
        response = self.rpgt_api_cli.post(POST_URL,
                                          REQUEST_DATA_CREATE_DUPLICATE,
                                          format="json",
                                          HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["bad_request"])

    def test_patch_item(self):
        """
        Submits a PATCH request against EDIT_URL + INSTANCE_ID
        """
        response = self.rpgt_api_cli.patch(EDIT_URL + INSTANCE_ID,
                                           REQUEST_DATA_PATCH,
                                           format="json",
                                           HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.json()['description'], TEST_VALUE)
        self.assertEqual(response.status_code, CODES["success"])

    def test_put_item(self):
        """
        Submits a PUT request against EDIT_URL + INSTANCE_ID
        """
        response = self.rpgt_api_cli.put(EDIT_URL + INSTANCE_ID,
                                         REQUEST_DATA_PUT,
                                         format="json",
                                         HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.json()['description'], TEST_VALUE)
        self.assertEqual(response.status_code, CODES["success"])

    def test_delete_item(self):
        """
        Submits a DELETE request against DELETE_URL + INSTANCE_ID
        """
        response = self.rpgt_api_cli.delete(DELETE_URL + INSTANCE_ID,
                                            HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["deleted"])


@tag("book_format_readonly")
class TestReadOnly(RpgtApiBTC):
    """
    Defines book_format test case class
    """
    fixtures = FIXTURES
    token = RpgtApiBTC.rpgt_api_cli.post(T_URL,
                                         RO_USER,
                                         format="json").json()["access"]

    # read-only user operations
    def test_get_item(self):
        """
        Submits a GET request against POST_URL
        Uses read-only creds
        """
        response = self.rpgt_api_cli.get(MODEL_URL,
                                         HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(len(response.json()), GET_COUNT)
        self.assertEqual(response.status_code, CODES["success"])

    def test_get_item_id(self):
        """
        Submits a GET request against POST_URL + INSTANCE_ID
        Uses read-only creds
        """
        response = self.rpgt_api_cli.get(POST_URL + INSTANCE_ID,
                                         HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.json()['id'], INSTANCE_ID)
        self.assertEqual(response.status_code, CODES["success"])

    def test_get_item_id_history(self):
        """
        Submits a GET request against POST_URL + INSTANCE_ID + '/history'
        Uses read-only creds
        """
        response = self.rpgt_api_cli.get(POST_URL + INSTANCE_ID + '/history',
                                         HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertTrue(response.json())
        self.assertEqual(response.status_code, CODES["success"])

    def test_post_item(self):
        """
        Submits a POST request against POST_URL
        Uses read-only creds
        """
        response = self.rpgt_api_cli.post(POST_URL,
                                          REQUEST_DATA_CREATE,
                                          format="json",
                                          HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["no_permission"])

    def test_patch_item(self):
        """
        Submits a PATCH request against EDIT_URL + INSTANCE_ID
        Uses read-only creds
        """
        response = self.rpgt_api_cli.patch(EDIT_URL + INSTANCE_ID,
                                           REQUEST_DATA_PATCH,
                                           format="json",
                                           HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["no_permission"])

    def test_put_item(self):
        """
        Submits a PUT request against EDIT_URL + INSTANCE_ID
        USES read-only creds
        """
        response = self.rpgt_api_cli.put(EDIT_URL + INSTANCE_ID,
                                         REQUEST_DATA_PUT,
                                         format="json",
                                         HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["no_permission"])

    def test_delete_item(self):
        """
        Submits a DELETE request against DELETE_URL + INSTANCE_ID
        Uses read-only creds
        """
        response = self.rpgt_api_cli.delete(DELETE_URL + INSTANCE_ID,
                                            HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["no_permission"])


@tag("book_format_anonymous")
class TestAnonymous(RpgtApiBTC):
    """
    Defines book_format test case class
    """
    fixtures = FIXTURES

    # anonymous user operations
    def test_get_item(self):
        """
        Submits a GET request against POST_URL
        Uses anonymouse access
        """
        response = self.rpgt_api_cli.get(MODEL_URL)
        self.assertEqual(len(response.json()), GET_COUNT)
        self.assertEqual(response.status_code, CODES["success"])

    def test_get_item_id(self):
        """
        Submits a GET request against POST_URL + INSTANCE_ID
        Uses anonymouse access
        """
        response = self.rpgt_api_cli.get(POST_URL + INSTANCE_ID)
        self.assertEqual(response.json()['id'], INSTANCE_ID)
        self.assertEqual(response.status_code, CODES["success"])

    def test_get_item_id_history(self):
        """
        Submits a GET request against POST_URL + INSTANCE_ID + '/history'
        Uses anonymouse access
        """
        response = self.rpgt_api_cli.get(POST_URL + INSTANCE_ID + '/history')
        self.assertTrue(response.json())
        self.assertEqual(response.status_code, CODES["success"])

    def test_post_item(self):
        """
        Submits a POST request against POST_URL
        Uses anonymouse access
        """
        response = self.rpgt_api_cli.post(POST_URL,
                                          REQUEST_DATA_CREATE,
                                          format="json")
        self.assertEqual(response.status_code, CODES["no_creds"])

    def test_patch_item(self):
        """
        Submits a PATCH request against EDIT_URL + INSTANCE_ID
        Uses anonymouse access
        """
        response = self.rpgt_api_cli.patch(EDIT_URL + INSTANCE_ID,
                                           REQUEST_DATA_PATCH,
                                           format="json")
        self.assertEqual(response.status_code, CODES["no_creds"])

    def test_put_item(self):
        """
        Submits a PUT request against EDIT_URL + INSTANCE_ID
        Uses anonymouse access
        """
        response = self.rpgt_api_cli.put(EDIT_URL + INSTANCE_ID,
                                         REQUEST_DATA_PUT,
                                         format="json")
        self.assertEqual(response.status_code, CODES["no_creds"])

    def test_delete_item(self):
        """
        Submits a DELETE request against DELETE_URL + INSTANCE_ID
        Uses anonymouse access
        """
        response = self.rpgt_api_cli.delete(DELETE_URL + INSTANCE_ID)
        self.assertEqual(response.status_code, CODES["no_creds"])
