# -*- coding: utf-8 -*- # pylint: disable=too-many-lines
"""
Defines test case run against the API for DieRoll model
"""
from django.test import tag
from api.tests.base import RPGToolsApiBaseTestCase
from api.tests.base import BASE_URL
from api.tests.base import CODES
from api.tests.base import READ_ONLY_USER
from api.tests.base import TOKEN_URL

MODEL_URL = BASE_URL + 'action-runner'

FIXTURES = ['test_users']

@tag("action_runner_readonly")
class TestPost(RPGToolsApiBaseTestCase):
    """Posts a json package to the action-runner url to test a specific use case.

    Attributes:
        JSON_INPUT [Static]: The json package to post to the target url
        ATTR_RANGE [Static]: Value range for some of the assertions involving
                             a specific value range.
    """
    fixtures = FIXTURES
    token = RPGToolsApiBaseTestCase.rpgtools_api_client.post(TOKEN_URL,
                                                             READ_ONLY_USER,
                                                             format="json").json()["access"]

    JSON_INPUT = {
        "action_input":  [
            {
                "name": "Fitness",
                "method": "die_roll",
                "input": {
                    "die_size": 6,
                    "die_count": 4,
                    "roll_modifier": {
                        "mod_type": "-",
                        "value": 4
                    },
                    "reroll": {
                        "condition": "==",
                        "value": 0
                    }
                }
            },
            {
                "name": "Agility",
                "method": "die_roll",
                "input": {
                    "die_size": 6,
                    "die_count": 4,
                    "roll_modifier": {
                        "mod_type": "-",
                        "value": 4
                    },
                    "reroll": {
                        "condition": "==",
                        "value": 0
                    }
                }
            },
            {
                "name": "Constitution",
                "method": "die_roll",
                "input": {
                    "die_size": 6,
                    "die_count": 4,
                    "roll_modifier": {
                        "mod_type": "-",
                        "value": 4
                    },
                    "reroll": {
                        "condition": "==",
                        "value": 0
                    }
                }
            },
            {
                "name": "Stature",
                "method": "die_roll",
                "input": {
                    "die_size": 6,
                    "die_count": 4,
                    "roll_modifier": {
                        "mod_type": "-",
                        "value": 4
                    },
                    "reroll": {
                        "condition": "==",
                        "value": 0
                    }
                }
            },
            {
                "name": "Intelligence",
                "method": "die_roll",
                "input": {
                    "die_size": 6,
                    "die_count": 4,
                    "roll_modifier": {
                        "mod_type": "-",
                        "value": 4
                    },
                    "reroll": {
                        "condition": "==",
                        "value": 0
                    }
                }
            },
            {
                "name": "Education",
                "method": "die_roll",
                "input": {
                    "die_size": 6,
                    "die_count": 4,
                    "roll_modifier": {
                        "mod_type": "-",
                        "value": 4
                    },
                    "reroll": {
                        "condition": "==",
                        "value": 0
                    }
                }
            }
        ]
    }
    ATTR_RANGE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    def test_run(self):
        """Executes a test against the target url using the defined json package."""
        response = self.rpgtools_api_client.post(MODEL_URL,
                                                    self.JSON_INPUT,
                                                    format="json",
                                                    HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["created"])
        self.assertTrue(response.json())
        self.assertTrue(response.json()['Fitness'])
        self.assertIn(response.json()['Fitness'],self.ATTR_RANGE)
        self.assertTrue(response.json()['Agility'])
        self.assertIn(response.json()['Agility'],self.ATTR_RANGE)
        self.assertTrue(response.json()['Constitution'])
        self.assertIn(response.json()['Constitution'],self.ATTR_RANGE)
        self.assertTrue(response.json()['Stature'])
        self.assertIn(response.json()['Stature'],self.ATTR_RANGE)
        self.assertTrue(response.json()['Intelligence'])
        self.assertIn(response.json()['Intelligence'],self.ATTR_RANGE)
        self.assertTrue(response.json()['Education'])
        self.assertIn(response.json()['Education'],self.ATTR_RANGE)
