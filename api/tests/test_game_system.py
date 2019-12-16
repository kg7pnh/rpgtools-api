# -*- coding: utf-8 -*-
"""
Defines test case run against the API for GameSystem model
"""
from django.test import tag
from api.tests.base import RPGToolsApiBaseTestCase
from api.tests.base import ADMIN_USER
from api.tests.base import BASE_URL
from api.tests.base import CODES
from api.tests.base import READ_ONLY_USER
from api.tests.base import TOKEN_URL

MODEL_URL = BASE_URL + 'gamesystems'
POST_URL = MODEL_URL + '/'
EDIT_URL = POST_URL + 'edit/'
DELETE_URL = POST_URL + 'delete/'

INSTANCE_ID = 'palladium-megaversal'
GET_COUNT = 5

FIXTURES = ['test_users',
    'test_publisher.json',
    'test_gamesystem.json']

CREATE_TEST_VALUE = 'test-game-system'
TEST_VALUE = 'UPDATED VIA TESTS'

REQUEST_DATA_CREATE = {
    "name": "Test Game System",
    "description": "Test Game System",
    "read_me": "Test Game System==---A test game system",
    "url": "https://www.google.com",
    "publisher": "e835030d-fbcf-4747-9dbf-fbb0e5e79f39",
    "short_name": "Test",
    "abbreviation": "TGS"
}

REQUEST_DATA_CREATE_DUPLICATE = {
    "name": "Palladium Megaversal",
    "description": "Also known as the Palladium Megaverse, this is a mostly unified system of rules for a wide range of games by the publisher Palladium Books.",
    "read_me": "Palladium Megaversal==---The **Megaversal system**, sometimes known as the **Palladium system**, is a set of mechanics specifically employed in most role-playing games published by Palladium Books, with the exception of *Recon*. It uses dice for roll-under percentile skill checks, roll-high combat checks and saving throws, and determination of damage (i.e. Mega Damage is to M.D.C. what \"damage\" is to S.D.C. ) sustained in melee encounters by which a character's Hit Points, Structural Damage Capacity (S.D.C.), or Mega-Damage Capacity (M.D.C.) is reduced accordingly.",
    "url": "https://rpggeek.com/rpgsystem/733/palladium-megaversal",
    "publisher": "e835030d-fbcf-4747-9dbf-fbb0e5e79f39",
    "short_name": "Megaversal",
    "abbreviation": "PALMGVL"
    }

REQUEST_DATA_PATCH = {
    "description": TEST_VALUE,
}

REQUEST_DATA_PUT = {
    "name": "Palladium Megaversal",
    "description": TEST_VALUE,
    "read_me": "Palladium Megaversal==---The **Megaversal system**, sometimes known as the **Palladium system**, is a set of mechanics specifically employed in most role-playing games published by Palladium Books, with the exception of *Recon*. It uses dice for roll-under percentile skill checks, roll-high combat checks and saving throws, and determination of damage (i.e. Mega Damage is to M.D.C. what \"damage\" is to S.D.C. ) sustained in melee encounters by which a character's Hit Points, Structural Damage Capacity (S.D.C.), or Mega-Damage Capacity (M.D.C.) is reduced accordingly.",
    "url": "https://rpggeek.com/rpgsystem/733/palladium-megaversal",
    "publisher": "e835030d-fbcf-4747-9dbf-fbb0e5e79f39",
    "short_name": "Megaversal",
    "abbreviation": "PALMGVL"
}

@tag("game_system_admin")
class TestAdmin(RPGToolsApiBaseTestCase):
    """
    Defines game_system test case class
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

    def test_get_item_id_history(self):
        """
        Submits a GET request against POST_URL + INSTANCE_ID + '/history'
        """
        response = self.rpgtools_api_client.get(POST_URL + INSTANCE_ID + '/history',
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
        self.assertEqual(response.status_code, CODES["bad_request"])

    def test_patch_item(self):
        """
        Submits a PATCH request against EDIT_URL + INSTANCE_ID
        """
        response = self.rpgtools_api_client.patch(EDIT_URL + INSTANCE_ID,
                                                  REQUEST_DATA_PATCH,
                                                  format="json",
                                                  HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.json()['description'], TEST_VALUE)
        self.assertEqual(response.status_code, CODES["success"])

    def test_put_item(self):
        """
        Submits a PUT request against EDIT_URL + INSTANCE_ID
        """
        response = self.rpgtools_api_client.put(EDIT_URL + INSTANCE_ID,
                                                REQUEST_DATA_PUT,
                                                format="json",
                                                HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.json()['description'], TEST_VALUE)
        self.assertEqual(response.status_code, CODES["success"])

    def test_delete_item(self):
        """
        Submits a DELETE request against DELETE_URL + INSTANCE_ID
        """
        response = self.rpgtools_api_client.delete(DELETE_URL + INSTANCE_ID,
                                                   HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["deleted"])

@tag("game_system_readonly")
class TestReadOnly(RPGToolsApiBaseTestCase):
    """
    Defines game_system test case class
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
        token = self.rpgtools_api_client_ro.post(TOKEN_URL,
                                                 READ_ONLY_USER,
                                                 format="json").json()["access"]
        response = self.rpgtools_api_client.get(MODEL_URL,
                                                HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(len(response.json()),GET_COUNT)
        self.assertEqual(response.status_code, CODES["success"])

    def test_get_item_id(self):
        """
        Submits a GET request against POST_URL + INSTANCE_ID
        Uses read-only creds
        """
        response = self.rpgtools_api_client.get(POST_URL + INSTANCE_ID,
                                                HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.json()['id'], INSTANCE_ID)
        self.assertEqual(response.status_code, CODES["success"])

    def test_get_item_id_history(self):
        """
        Submits a GET request against POST_URL + INSTANCE_ID + '/history'
        Uses read-only creds
        """
        response = self.rpgtools_api_client.get(POST_URL + INSTANCE_ID + '/history',
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
        Submits a PATCH request against EDIT_URL + INSTANCE_ID
        Uses read-only creds
        """
        response = self.rpgtools_api_client.patch(EDIT_URL + INSTANCE_ID,
                                                  REQUEST_DATA_PATCH,
                                                  format="json",
                                                  HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["no_permission"])

    def test_put_item(self):
        """
        Submits a PUT request against EDIT_URL + INSTANCE_ID
        USES read-only creds
        """
        response = self.rpgtools_api_client.put(EDIT_URL + INSTANCE_ID,
                                                REQUEST_DATA_PUT,
                                                format="json",
                                                HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["no_permission"])

    def test_delete_item(self):
        """
        Submits a DELETE request against DELETE_URL + INSTANCE_ID
        Uses read-only creds
        """
        response = self.rpgtools_api_client.delete(DELETE_URL + INSTANCE_ID,
                                                   HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["no_permission"])

@tag("game_system_anonymous")
class TestAnonymous(RPGToolsApiBaseTestCase):
    """
    Defines game_system test case class
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

    def test_get_item_id_history(self):
        """
        Submits a GET request against POST_URL + INSTANCE_ID + '/history'
        Uses anonymouse access
        """
        response = self.rpgtools_api_client.get(POST_URL + INSTANCE_ID + '/history')
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
        Submits a PATCH request against EDIT_URL + INSTANCE_ID
        Uses anonymouse access
        """
        response = self.rpgtools_api_client.patch(EDIT_URL + INSTANCE_ID,
                                                  REQUEST_DATA_PATCH,
                                                  format="json")
        self.assertEqual(response.status_code, CODES["no_creds"])

    def test_put_item(self):
        """
        Submits a PUT request against EDIT_URL + INSTANCE_ID
        Uses anonymouse access
        """
        response = self.rpgtools_api_client.put(EDIT_URL + INSTANCE_ID,
                                                REQUEST_DATA_PUT,
                                                format="json")
        self.assertEqual(response.status_code, CODES["no_creds"])

    def test_delete_item(self):
        """
        Submits a DELETE request against DELETE_URL + INSTANCE_ID
        Uses anonymouse access
        """
        response = self.rpgtools_api_client.delete(DELETE_URL + INSTANCE_ID)
        self.assertEqual(response.status_code, CODES["no_creds"])
