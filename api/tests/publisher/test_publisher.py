# -*- coding: utf-8 -*-
"""
Defines test case run against the API for Publisher model
"""
from django.test import tag
from api.tests.base import RpgtApiBTC
from api.tests.base import ADMIN_USER
from api.tests.base import API_URL
from api.tests.base import CODES
from api.tests.base import RO_USER
from api.tests.base import T_URL

MODEL_URL = API_URL + 'publishers'
POST_URL = MODEL_URL + '/'
EDIT_URL = POST_URL + 'edit/'
DELETE_URL = POST_URL + 'delete/'

INSTANCE_ID = 'steve-jackson-games'
GET_COUNT = 12

FIXTURES = ['test_users',
            'test_publisher.json']

CREATE_TEST_VALUE = 'test-publisher'
TEST_VALUE = 'UPDATED VIA TESTS'

REQUEST_DATA_CREATE = {
    "name": "Test Publisher",
    "description": "A Test Publisher",
    "read_me": "Test Publisher==---A test publisher.",
    "url": "https://rpggeek.com/rpg/511/rifts",
    "abbreviation": "TP"
}

REQUEST_DATA_CREATE_DUPLICATE = {
    "name": "Steve Jackson Games",
    "description": "Well known for their GURPS system as well as Munchkin.",
    "read_me": "Steve Jackson Games\n==\n---\n&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Steve Jackson Games** (**SJGames**) is a game company, founded in 1980 by Steve Jackson, that creates and publishes role-playing, board, and card games, and the gaming magazine Pyramid.", # pylint: disable=line-too-long
    "url": "http://www.sjgames.com/",
    "abbreviation": "SJGames"
}

REQUEST_DATA_PATCH = {
    "description": TEST_VALUE,
}

REQUEST_DATA_PUT = {
    "name": "Steve Jackson Games",
    "description": TEST_VALUE,
    "read_me": "Steve Jackson Games\n==\n---\n&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Steve Jackson Games** (**SJGames**) is a game company, founded in 1980 by Steve Jackson, that creates and publishes role-playing, board, and card games, and the gaming magazine Pyramid.", # pylint: disable=line-too-long
    "url": "http://www.sjgames.com/",
    "abbreviation": "SJGames"
}

@tag("publisher_admin")
class TestAdmin(RpgtApiBTC):
    """
    Defines publisher test case class
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

@tag("publisher_readonly")
class TestReadOnly(RpgtApiBTC):
    """
    Defines publisher test case class
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

@tag("publisher_anonymous")
class TestAnonymous(RpgtApiBTC):
    """
    Defines publisher test case class
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
