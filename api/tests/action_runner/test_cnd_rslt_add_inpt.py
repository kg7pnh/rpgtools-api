# -*- coding: utf-8 -*- # pylint: disable=too-many-lines
"""Defines test case run against the API for DieRoll model
"""
from django.test import tag
from api.tests.base import RpgtApiBTC
from api.tests.base import API_URL
from api.tests.base import CODES

MODEL_URL = API_URL + 'action-runner'


@tag("action_runner_anonymous")
class TestPost(RpgtApiBTC):
    # TODO: update docstring
    """Posts a json package to the action-runner url to test a specific use case.

    Attributes:
        JSON_INPUT [Static]: The json package to post to the target url
    """
    JSON_INPUT = {
        "action_input":  [
            {
                "name": "test_case",
                "method": "conditional",
                "input": {
                    "test_value": 6,
                    "conditions": {
                        "0": {
                            "test": "==",
                            "eval": 6,
                            "result": "test"
                        }
                    }
                }
            }
        ],
        "additional_input": {
            "test": 0
        }
    }

    def test_run(self):
        # TODO: update docstring
        """Executes a test against the target url using the defined json package
        """
        response = self.rpgt_api_cli.post(MODEL_URL,
                                          self.JSON_INPUT,
                                          format="json")
        self.assertEqual(response.status_code, CODES["created"])
        self.assertEqual(response.json()['test_case'], 0)
