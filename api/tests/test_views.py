# -*- coding: utf-8 -*-
"""
Defines test case run against the API for DieRoll model
"""
from django.test import tag
from api.tests.base import RPGToolsApiBaseTestCase
from api.tests.base import ADMIN_USER
from api.tests.base import BASE_URL
from api.tests.base import CODES
from api.tests.base import READ_ONLY_USER
from api.tests.base import TOKEN_URL

FIXTURES = ['test_users']

ACTION_RUNNER_INPUT = {
    "action_input": {
        "fitness": {
            "method": "die_roll",
            "input": {
                "die_size": 6,
                "die_count": 4,
                "roll_modifier": {
                    "type": "-",
                    "value": 4
                },
                "reroll": {
                    "condition": "==",
                    "value": 0
                }
            }
        },
        "agility": {
            "method": "die_roll",
            "input": {
                "die_size": 6,
                "die_count": 4,
                "roll_modifier": {
                    "type": "-",
                    "value": 4
                },
                "reroll": {
                    "condition": "==",
                    "value": 0
                }
            }
        },
        "constitution": {
            "method": "die_roll",
            "input": {
                "die_size": 6,
                "die_count": 4,
                "roll_modifier": {
                    "type": "-",
                    "value": 4
                },
                "reroll": {
                    "condition": "==",
                    "value": 0
                }
            }
        },
        "stature": {
            "method": "die_roll",
            "input": {
                "die_size": 6,
                "die_count": 4,
                "roll_modifier": {
                    "type": "-",
                    "value": 4
                },
                "reroll": {
                    "condition": "==",
                    "value": 0
                }
            }
        },
        "intelligence": {
            "method": "die_roll",
            "input": {
                "die_size": 6,
                "die_count": 4,
                "roll_modifier": {
                    "type": "-",
                    "value": 4
                },
                "reroll": {
                    "condition": "==",
                    "value": 0
                }
            }
        },
        "education": {
            "method": "die_roll",
            "input": {
                "die_size": 6,
                "die_count": 4,
                "roll_modifier": {
                    "type": "-",
                    "value": 4
                },
                "reroll": {
                    "condition": "==",
                    "value": 0
                }
            }
        }
    }
}

@tag("views_admin")
class TestsAdmin(RPGToolsApiBaseTestCase):
    """
    Defines TestAdmin class
    """
    fixtures = FIXTURES
    response = RPGToolsApiBaseTestCase.rpgtools_api_client.post(TOKEN_URL,
                                                                ADMIN_USER,
                                                                format="json").json()
    token = response['access']
    refresh = response['refresh']

    def test_get_current_user(self):
        """
        Submits a POST request
        """
        response = self.rpgtools_api_client.get(BASE_URL + '/current-user',
                                                HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["success"])
        self.assertEqual(response.json()['is_authenticated'], True)
        self.assertEqual(response.json()['username'], 'admin')
        self.assertEqual(response.json()['first_name'], 'admin')
        self.assertEqual(response.json()['last_name'], 'admin')
        self.assertEqual(response.json()['is_superuser'], True)

    def test_get_is_admin(self):
        """
        Submits a POST request
        """
        response = self.rpgtools_api_client.get(BASE_URL + '/is-admin',
                                                HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["success"])

    def test_post_token(self):
        """
        Submits a POST request
        """
        response = self.rpgtools_api_client.post(TOKEN_URL,
                                                ADMIN_USER,
                                                format="json")
        self.assertEqual(response.status_code, CODES["success"])
        self.assertTrue(response.json()['access'])

    def test_post_token_refresh(self):
        """
        Submits a POST request
        """
        response = self.rpgtools_api_client.post(TOKEN_URL + '/refresh',
                                                 { "refresh": self.refresh},
                                                 format="json")
        self.assertEqual(response.status_code, CODES["success"])
        self.assertTrue(response.json()['access'])

    def test_post_token_verify(self):
        """
        Submits a POST request
        """
        response = self.rpgtools_api_client.post(TOKEN_URL + '/refresh/',
                                                 { "token": self.token},
                                                 format="json")
        self.assertEqual(response.status_code, CODES["success"])
        self.assertFalse(response.json())

@tag("views_readonly")
class TestsReadOnly(RPGToolsApiBaseTestCase):
    """
    Defines TestsReadOnly class
    """
    fixtures = FIXTURES
    response = RPGToolsApiBaseTestCase.rpgtools_api_client.post(TOKEN_URL,
                                                                READ_ONLY_USER,
                                                                format="json").json()
    token = response['access']
    refresh = response['refresh']

    def test_get_current_user(self):
        """
        Submits a POST request
        """
        response = self.rpgtools_api_client.get(BASE_URL + '/current-user',
                                                 HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["success"])
        self.assertEqual(response.json()['is_authenticated'], True)
        self.assertEqual(response.json()['username'], 'read-only')
        self.assertEqual(response.json()['first_name'], 'read')
        self.assertEqual(response.json()['last_name'], 'only')
        self.assertEqual(response.json()['is_superuser'], False)

    def test_get_is_admin(self):
        """
        Submits a POST request
        """
        response = self.rpgtools_api_client.get(BASE_URL + '/is-admin',
                                                 HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["no_permission"])

    def test_post_token(self):
        """
        Submits a POST request against MODEL_URL
        Validates admin access
        """
        response = self.rpgtools_api_client.post(TOKEN_URL,
                                                READ_ONLY_USER,
                                                format="json")
        self.assertEqual(response.status_code, CODES["success"])
        self.assertTrue(response.json()['access'])

    def test_post_token_refresh(self):
        """
        Submits a POST request against MODEL_URL
        Validates admin access
        """
        response = self.rpgtools_api_client.post(TOKEN_URL + '/refresh',
                                                 { "refresh": self.refresh},
                                                 format="json")
        self.assertEqual(response.status_code, CODES["success"])
        self.assertTrue(response.json()['access'])

    def test_post_token_verify(self):
        """
        Submits a POST request against MODEL_URL
        Validates admin access
        """
        response = self.rpgtools_api_client.post(TOKEN_URL + '/refresh/',
                                                 { "token": self.token},
                                                 format="json")
        self.assertEqual(response.status_code, CODES["success"])
        self.assertFalse(response.json())

@tag("views_anonymous")
class TestsAnonymous(RPGToolsApiBaseTestCase):
    """
    Defines TestsAnonymous class
    """

    def test_get_current_user(self):
        """
        Submits a POST request
        """
        response = self.rpgtools_api_client.get(BASE_URL + '/current-user')
        self.assertEqual(response.status_code, CODES["success"])
        self.assertEqual(response.json()['is_authenticated'], False)
        self.assertEqual(response.json()['username'], None)
        self.assertEqual(response.json()['first_name'], None)
        self.assertEqual(response.json()['last_name'], None)
        self.assertEqual(response.json()['is_superuser'], None)

    def test_get_is_admin(self):
        """
        Submits a POST request
        """
        response = self.rpgtools_api_client.get(BASE_URL + '/is-admin')
        self.assertEqual(response.status_code, CODES["no_creds"])
