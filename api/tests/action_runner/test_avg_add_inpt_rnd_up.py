# -*- coding: utf-8 -*- # pylint: disable=too-many-lines
"""
Defines test case run against the API for DieRoll model
"""
from django.test import tag
from api.tests.base import RpgtApiBTC
from api.tests.base import API_URL
from api.tests.base import CODES

MODEL_URL = API_URL + 'action-runner'

@tag("action_runner_anonymous")
class TestPost(RpgtApiBTC):
    """Posts a json package to the action-runner url to test a specific use case.

    Attributes:
        JSON_INPUT [Static]: The json package to post to the target url
    """
    JSON_INPUT = {
        "action_input": [
            {
                "name": "test_case",
                "method": "average",
                "input": {
                    "round": "up",
                    "0": 100,
                    "1": 51,
                    "2": 12,
                    "3": "test_1",
                    "4": "test_2"
                }
            }
        ],
        "additional_input": {
            "test_1": 5,
            "test_2": 6
        }
    }

    def test_run(self):
        """Executes a test against the target url using the defined json package"""
        response = self.rpgt_api_cli.post(MODEL_URL,
                                                 self.JSON_INPUT,
                                                 format="json")
        self.assertEqual(response.status_code, CODES["created"])
        self.assertEqual(response.json()["test_case"], 35)
