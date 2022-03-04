# -*- coding: utf-8 -*-
"""
Defines test case run against the API for Game model
"""
from django.test import tag
from api.tests.base import RpgtApiBTC
from api.tests.base import ADMIN_USER
from api.tests.base import API_URL
from api.tests.base import CODES
from api.tests.base import RO_USER
from api.tests.base import T_URL

MODEL_URL = API_URL + 'games'
POST_URL = MODEL_URL + '/'
EDIT_URL = POST_URL + 'edit/'
DELETE_URL = POST_URL + 'delete/'

INSTANCE_ID = 'rifts'
GET_COUNT = 4

FIXTURES = ['test_users',
            'test_publisher.json',
            'test_gamesystem.json',
            'test_game.json']

CREATE_TEST_VALUE = 'test-game'
TEST_VALUE = 'UPDATED VIA TESTS'

REQUEST_DATA_CREATE = {
    "name": "Test Game",
    "description": "A Test Game",
    "read_me": "Test Game==---A test game.",
    "url": "https://rpggeek.com/rpg/511/rifts",
    "game_system": "20f5f42b-9531-47e0-a794-f6607e9520b5",
    "publisher": "e835030d-fbcf-4747-9dbf-fbb0e5e79f39",
    "short_name": "Test",
    "abbreviation": "TG"
}

REQUEST_DATA_CREATE_DUPLICATE = {
    "name": "Rifts",
    "description": "The Rifts Rpg is a multi-genre role-playing game that captures the elements of magic and the supernatural along with science fiction and high technology", # pylint: disable=line-too-long
    "read_me": "Rifts\n==\n---\n**_Rifts_** is a multi-genre role-playing game created by Kevin Siembieda in August 1990 and published continuously by Palladium Books since then. *Rifts* takes place in a post-apocalyptic future, deriving elements from cyberpunk, science fiction, fantasy, horror, western, mythology and many other genres.\n\n*Rifts* serves as a cross-over environment for a variety of other Palladium games with different universes connected through \"rifts\" on Earth that lead to different spaces, times, and realities that Palladium calls the \"Rifts Megaverse\". \n*Rifts* describes itself as an \"advanced\" role-playing game and not an introduction for those new to the concept.\n\nChanged\n\nPalladium continues to publish books for the Rifts series, with about 80 books published between 1990 and 2011. *Rifts Ultimate Edition* was released in August 2005 and designed to update the game with Palladium's incremental changes to its system, changes in the game world, and additional information and character types. The web site is quick to point out that this is not a second edition but an improvement and expansion of the original role playing game.", # pylint: disable=line-too-long
    "url": "https://rpggeek.com/rpg/511/rifts",
    "game_system": "20f5f42b-9531-47e0-a794-f6607e9520b5",
    "publisher": "e835030d-fbcf-4747-9dbf-fbb0e5e79f39",
    "short_name": "Rifts",
    "abbreviation": "RFTS"
}

REQUEST_DATA_PATCH = {
    "description": TEST_VALUE,
}

REQUEST_DATA_PUT = {
    "name": "Rifts",
    "description": TEST_VALUE,
    "read_me": "Rifts\n==\n---\n**_Rifts_** is a multi-genre role-playing game created by Kevin Siembieda in August 1990 and published continuously by Palladium Books since then. *Rifts* takes place in a post-apocalyptic future, deriving elements from cyberpunk, science fiction, fantasy, horror, western, mythology and many other genres.\n\n*Rifts* serves as a cross-over environment for a variety of other Palladium games with different universes connected through \"rifts\" on Earth that lead to different spaces, times, and realities that Palladium calls the \"Rifts Megaverse\". \n*Rifts* describes itself as an \"advanced\" role-playing game and not an introduction for those new to the concept.\n\nChanged\n\nPalladium continues to publish books for the Rifts series, with about 80 books published between 1990 and 2011. *Rifts Ultimate Edition* was released in August 2005 and designed to update the game with Palladium's incremental changes to its system, changes in the game world, and additional information and character types. The web site is quick to point out that this is not a second edition but an improvement and expansion of the original role playing game.", # pylint: disable=line-too-long
    "url": "https://rpggeek.com/rpg/511/rifts",
    "game_system": "20f5f42b-9531-47e0-a794-f6607e9520b5",
    "publisher": "e835030d-fbcf-4747-9dbf-fbb0e5e79f39",
    "short_name": "Rifts",
    "abbreviation": "RFTS"
}

@tag("game_admin")
class TestAdmin(RpgtApiBTC):
    """
    Defines game test case class
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

@tag("game_readonly")
class TestReadOnly(RpgtApiBTC):
    """
    Defines game test case class
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

@tag("game_anonymous")
class TestAnonymous(RpgtApiBTC):
    """
    Defines game test case class
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
