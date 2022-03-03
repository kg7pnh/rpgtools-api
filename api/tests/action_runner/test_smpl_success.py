# -*- coding: utf-8 -*- # pylint: disable=too-many-lines
"""
Defines test case run against the API for DieRoll model
"""
from django.test import tag
from api.tests.base import RPGToolsApiBaseTestCase
from api.tests.base import BASE_URL
from api.tests.base import CODES

MODEL_URL = BASE_URL + 'action-runner'

@tag("action_runner_anonymous")
class TestPost(RPGToolsApiBaseTestCase):
    """Posts a json package to the action-runner url to test a specific use case.

    Attributes:
        JSON_INPUT [Static]: The json package to post to the target url
    """
    JSON_INPUT = {
        "action_input":  [
            {
                "name": "test_case",
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

    def test_run(self):
        """Executes a test against the target url using the defined json package 1000 times."""
        for iteration in range(1000): # pylint: disable=unused-variable
            response = self.rpgtools_api_client.post(MODEL_URL,
                                                     self.JSON_INPUT,
                                                     format="json")
            self.assertEqual(response.status_code, CODES["created"])
            self.assertGreaterEqual(response.json()['test_case'], 1)
            self.assertLessEqual(response.json()['test_case'], 20)
