# -*- coding: utf-8 -*-
"""Defines test case run against the API for DieRoll model
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
        """Executes a test against the target url using the defined json package
        """
        response = self.rpgt_api_cli.post(MODEL_URL,
                                          self.JSON_INPUT,
                                          format="json")
        self.assertEqual(response.status_code, CODES["created"])
        self.assertEqual(response.json()["error_entry_index_0"],
                         "Action Input entries require \"name\", \"method\""
                         " and \"input\" items to be processed.")
