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
    JSON_INPUT:dict = {
        "action_input": [
            {
                "name": "test_case",
                "method": "table",
                "input": {
                    "style": "simple",
                    "choice": "7",
                    "choices": {
                        "-1": "2nd Lieutenant",
                        "0": "2nd Lieutenant",
                        "1": "2nd Lieutenant",
                        "2": "1st Lieutenant",
                        "3": "1st Lieutenant",
                        "4": "Captain",
                        "5": "Captain",
                        "6": "Major",
                        "7": "Major",
                        "8": "Lieutenant Colonel"
                    }
                }
            }
        ]
    }

    def test_run(self):
        """Executes a test against the target url using the defined json package"""
        response = self.rpgtools_api_client.post(MODEL_URL,
                                                 self.JSON_INPUT,
                                                 format="json")
        self.assertEqual(response.status_code, CODES["created"])
        self.assertEqual(response.json()["test_case"], "Major")
