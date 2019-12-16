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

MODEL_URL = BASE_URL + 'action-runner'

FIXTURES = ['test_users']

ACTION_RUNNER_INPUT_SIMPLE_SUCCESSFULL = {
    "action_input": {
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

ACTION_RUNNER_INPUT_LARGE_SUCCESSFULL = {
    "action_input": {
        "Fitness": {
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
        "Agility": {
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
        "Constitution": {
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
        "Stature": {
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
        "Intelligence": {
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
        "Education": {
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

ACTION_RUNNER_INPUT_COMPLEX_SUCCESSFULL = {
    "action_input": {
        "Fitness": {
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
        "Agility": {
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
        "Constitution": {
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
        "Stature": {
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
        "Intelligence": {
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
        "Education": {
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
        "Total": {
            "method": "calculation",
            "input": {
                "formula": {
                    "0": "Fitness",
                    "1": "+",
                    "2": "Agility",
                    "3": "+",
                    "4": "Constitution",
                    "5": "+",
                    "6": "Stature",
                    "7": "+",
                    "8": "Intelligence",
                    "9": "+",
                    "10": "Education"
                },
                "round": "drop"
            }
        },
        "Strength": {
            "method": "calculation",
            "input": {
                "formula": {
                    "0": "(",
                    "1": "Fitness",
                    "2": "+",
                    "3": "Stature",
                    "4": ")",
                    "5": "/",
                    "6": 2
                },
                "round": "down"
            }
        },
        "Hit Capacity - Head": {
            "method": "calculation",
            "input": {
                "formula": {
                    "0": "Constitution"
                }
            }
        },
        "Hit Capacity - Chest": {
            "method": "calculation",
            "input": {
                "formula": {
                    "0": "Strength",
                    "1": "+",
                    "2": "Constitution",
                    "3": "+",
                    "4": "Stature"
                }
            }
        },
        "Hit Capacity - Other": {
            "method": "calculation",
            "input": {
                "formula": {
                    "0": "Constitution",
                    "1": "+",
                    "2": "Stature"
                }
            }
        },
        "Weight": {
            "method": "calculation",
            "input": {
                "formula": {
                    "0": 40,
                    "1": "+",
                    "2": 4,
                    "3": "*",
                    "4": "Stature"
                }
            }
        },
        "Load": {
            "method": "calculation",
            "input": {
                "formula": {
                    "0": "Strength",
                    "1": "+",
                    "2": "Constitution",
                    "3": "+",
                    "4": "Stature"
                }
            }
        },
        "Throw Range": {
            "method": "calculation",
            "input": {
                "formula": {
                    "0": "Strength",
                    "1": "*",
                    "2": 2
                }
            }
        },
        "Military Experience Base": {
            "method": "calculation",
            "input": {
                "formula": {
                    "0": "(",
                    "1": 120,
                    "2": "-",
                    "3": "Total",
                    "4": ")",
                    "5": "/",
                    "6": 7
                },
                "round": "down"
            }
        },
        "Time In Combat": {
            "method": "die_roll",
            "input": {
                "die_size": 6,
                "die_count": "Military Experience Base"
            }
        },
        "Coolness": {
            "method": "calculation",
            "input": {
                "formula": {
                    "0": 10,
                    "1": "-",
                    "2": "int",
                    "3": "(",
                    "4": "Time In Combat",
                    "5": "/",
                    "6": 10,
                    "7": "+",
                    "8": {
                        "die_roll": {
                            "input": {
                                "die_size": 6,
                                "die_count": 1
                            }
                        }
                    },
                    "9": ")"
                }
            }
        },
        "RADS": {
            "method": "die_roll",
            "input": {
                "die_size": 6,
                "die_count": "Military Experience Base"
            }
        },
        "Age": {
            "method": "calculation",
            "input": {
                "formula": {
                    "0": "Education",
                    "1": "+",
                    "2": 8,
                    "3": "+",
                    "4": "math.ceil",
                    "5": "(",
                    "6": "Time In Combat",
                    "7": "/",
                    "8": 12,
                    "9": ")",
                    "10": "+",
                    "11": {
                        "conditional": {
                            "input": {
                                "test_value": "Time In Combat",
                                "conditions": {
                                    "0": {
                                        "test": ">=",
                                        "eval": 70,
                                        "result": {
                                            "die_roll": {
                                                "input": {
                                                    "die_size": 6,
                                                    "die_count": 4
                                                }
                                            }
                                        }
                                    },
                                    "1": {
                                        "test": ">=",
                                        "eval": 60,
                                        "result": {
                                            "die_roll": {
                                                "input": {
                                                    "die_size": 6,
                                                    "die_count": 3
                                                }
                                            }
                                        }
                                    },
                                    "2": {
                                        "test": ">=",
                                        "eval": 50,
                                        "result": {
                                            "die_roll": {
                                                "input": {
                                                    "die_size": 6,
                                                    "die_count": 2
                                                }
                                            }
                                        }
                                    },
                                    "3": {
                                        "test": "<",
                                        "eval": 50,
                                        "result": {
                                            "die_roll": {
                                                "input": {
                                                    "die_size": 6,
                                                    "die_count": 1
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "Officer": {
            "method": "conditional",
            "input": {
                "test_value": {
                    "die_roll": {
                        "input": {
                            "die_size": 6,
                            "die_count": 1,
                            "roll_modifier": {
                                "type": "+",
                                "value": 16
                            }
                        }
                    }
                },
                "conditions": {
                    "0": {
                        "test": "<=",
                        "eval": {
                            "calculation": {
                                "input": {
                                    "formula": {
                                        "0": "Education",
                                        "1": "+",
                                        "2": "Intelligence"
                                    }
                                }
                            }
                        },
                        "result": True
                    },
                    "1": {
                        "test": ">",
                        "eval": {
                            "calculation": {
                                "input": {
                                    "formula": {
                                        "0": "Education",
                                        "1": "+",
                                        "2": "Intelligence"
                                    }
                                }
                            }
                        },
                        "result": False
                    }
                }
            }
        },
        "Rank Number": {
            "method": "calculation",
            "input": {
                "formula": {
                    "0": "math.trunc",
                    "1": "(",
                    "2": "Time In Combat",
                    "3": "/",
                    "4": 10,
                    "5": ")",
                    "6": "+",
                    "7": {
                        "conditional": {
                            "input": {
                                "test_value": {
                                    "die_roll": {
                                        "input": {
                                            "die_size": 6,
                                            "die_count": 1
                                        }
                                    }
                                },
                                "conditions": {
                                    "0": {
                                        "test": "<=",
                                        "eval": 2,
                                        "result": -1
                                    },
                                    "1": {
                                        "test": ">=",
                                        "eval": 3,
                                        "result": 0
                                    },
                                    "2": {
                                        "test": ">=",
                                        "eval": 5,
                                        "result": 1
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "Rank": {
            "method": "conditional",
            "input": {
                "test_value": "Officer",
                "conditions": {
                    "0": {
                        "test": "==",
                        "eval": True,
                        "result": {
                            "table": {
                                "input": {
                                    "style": "simple",
                                    "choice": "Rank Number",
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
                        }
                    },
                    "1": {
                        "test": "==",
                        "eval": False,
                        "result": {
                            "table": {
                                "input": {
                                    "style": "simple",
                                    "choice": "Rank Number",
                                    "choices": {
                                        "-1": "Spec 4",
                                        "0": "Spec 4",
                                        "1": "Spec 4",
                                        "2": "Spec 4",
                                        "3": "Sergeant",
                                        "4": "Sergeant",
                                        "5": "Staff Sergeant",
                                        "6": "Platoon Sergeant",
                                        "7": "Master Sergeant",
                                        "8": "Sergeant Major"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

        # "Coolness D6": {
        #     "method": "die_roll",
        #     "input": {
        #         "die_size": 6,
        #         "die_count": 1,
        #         "roll_modifier": {
        #             "type": "+",
        #             "value": "Coolness Base"
        #         }
        #     }
        # },
        # "Coolness":{
        #     "method": "calculation",
        #     "input": {
        #         "formula": [
        #             10,
        #             "-",
        #             "Coolness D6"
        #         ]
        #     }
        # },

ACTION_RUNNER_INPUT_SIMPLE_FAIL_IMPORT = {
    "action_input": {
        "method": "foo_bar",
        "input": {
            "foo": "bar"
        } 
    }
}

@tag("action_runner_admin")
class TestAdmin(RPGToolsApiBaseTestCase):
    """
    Defines die_roll test case class
    """
    fixtures = FIXTURES
    token = RPGToolsApiBaseTestCase.rpgtools_api_client.post(TOKEN_URL,
                                                             ADMIN_USER,
                                                             format="json").json()["access"]

    def test_post_success(self):
        """
        Submits a POST request against MODEL_URL
        Validates admin access
        """
        response = self.rpgtools_api_client.post(MODEL_URL,
                                                 ACTION_RUNNER_INPUT_LARGE_SUCCESSFULL,
                                                 format="json",
                                                 HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["created"]) 
        self.assertTrue(response.json())
        self.assertTrue(response.json()['Fitness'])
        self.assertGreaterEqual(response.json()['Fitness'], 1)
        self.assertLessEqual(response.json()['Fitness'], 20)
        self.assertTrue(response.json()['Agility'])
        self.assertGreaterEqual(response.json()['Agility'], 1)
        self.assertLessEqual(response.json()['Agility'], 20)
        self.assertTrue(response.json()['Constitution'])
        self.assertGreaterEqual(response.json()['Constitution'], 1)
        self.assertLessEqual(response.json()['Constitution'], 20)
        self.assertTrue(response.json()['Stature'])
        self.assertGreaterEqual(response.json()['Stature'], 1)
        self.assertLessEqual(response.json()['Stature'], 20)
        self.assertTrue(response.json()['Intelligence'])
        self.assertGreaterEqual(response.json()['Intelligence'], 1)
        self.assertLessEqual(response.json()['Intelligence'], 20)
        self.assertTrue(response.json()['Education'])
        self.assertGreaterEqual(response.json()['Education'], 1)
        self.assertLessEqual(response.json()['Education'], 20)

@tag("action_runner_readonly")
class TestReadOnly(RPGToolsApiBaseTestCase):
    """
    Defines die_roll test case class
    """
    fixtures = FIXTURES
    token = RPGToolsApiBaseTestCase.rpgtools_api_client.post(TOKEN_URL,
                                                             READ_ONLY_USER,
                                                             format="json").json()["access"]

    def test_post_success(self):
        """
        Submits a POST request against MODEL_URL
        """
        response = self.rpgtools_api_client.post(MODEL_URL,
                                                 ACTION_RUNNER_INPUT_LARGE_SUCCESSFULL,
                                                 format="json",
                                                 HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["created"]) 
        self.assertTrue(response.json())
        self.assertTrue(response.json()['Fitness'])
        self.assertGreaterEqual(response.json()['Fitness'], 1)
        self.assertLessEqual(response.json()['Fitness'], 20)
        self.assertTrue(response.json()['Agility'])
        self.assertGreaterEqual(response.json()['Agility'], 1)
        self.assertLessEqual(response.json()['Agility'], 20)
        self.assertTrue(response.json()['Constitution'])
        self.assertGreaterEqual(response.json()['Constitution'], 1)
        self.assertLessEqual(response.json()['Constitution'], 20)
        self.assertTrue(response.json()['Stature'])
        self.assertGreaterEqual(response.json()['Stature'], 1)
        self.assertLessEqual(response.json()['Stature'], 20)
        self.assertTrue(response.json()['Intelligence'])
        self.assertGreaterEqual(response.json()['Intelligence'], 1)
        self.assertLessEqual(response.json()['Intelligence'], 20)
        self.assertTrue(response.json()['Education'])
        self.assertGreaterEqual(response.json()['Education'], 1)
        self.assertLessEqual(response.json()['Education'], 20)

@tag("action_runner_anonymous")
class TestAnonymous(RPGToolsApiBaseTestCase):
    """
    Defines die_roll test case class for anonymous access
    """

    def test_post_simple_success(self):
        """
        """
        for x in range(1000):
            response = self.rpgtools_api_client.post(MODEL_URL,
                                                    ACTION_RUNNER_INPUT_SIMPLE_SUCCESSFULL,
                                                    format="json")
            self.assertEqual(response.status_code, CODES["created"]) 


    def test_post_large_success(self):
        """
        Submits a POST request against MODEL_URL
        """
        for x in range(1000):
            response = self.rpgtools_api_client.post(MODEL_URL,
                                                    ACTION_RUNNER_INPUT_LARGE_SUCCESSFULL,
                                                    format="json")
            self.assertEqual(response.status_code, CODES["created"]) 
            self.assertTrue(response.json())
            self.assertTrue(response.json()['Fitness'])
            self.assertGreaterEqual(response.json()['Fitness'], 1)
            self.assertLessEqual(response.json()['Fitness'], 20)
            self.assertTrue(response.json()['Agility'])
            self.assertGreaterEqual(response.json()['Agility'], 1)
            self.assertLessEqual(response.json()['Agility'], 20)
            self.assertTrue(response.json()['Constitution'])
            self.assertGreaterEqual(response.json()['Constitution'], 1)
            self.assertLessEqual(response.json()['Constitution'], 20)
            self.assertTrue(response.json()['Stature'])
            self.assertGreaterEqual(response.json()['Stature'], 1)
            self.assertLessEqual(response.json()['Stature'], 20)
            self.assertTrue(response.json()['Intelligence'])
            self.assertGreaterEqual(response.json()['Intelligence'], 1)
            self.assertLessEqual(response.json()['Intelligence'], 20)
            self.assertTrue(response.json()['Education'])
            self.assertGreaterEqual(response.json()['Education'], 1)
            self.assertLessEqual(response.json()['Education'], 20)

    def test_post_complex_success(self):
        """
        Submits a POST request against MODEL_URL
        """
        response = self.rpgtools_api_client.post(MODEL_URL,
                                                 ACTION_RUNNER_INPUT_COMPLEX_SUCCESSFULL,
                                                 format="json")
        self.assertEqual(response.status_code, CODES["created"]) 
        self.assertTrue(response.json())
        self.assertTrue(response.json()['Fitness'])
        self.assertGreaterEqual(response.json()['Fitness'], 1)
        self.assertLessEqual(response.json()['Fitness'], 20)
        self.assertTrue(response.json()['Agility'])
        self.assertGreaterEqual(response.json()['Agility'], 1)
        self.assertLessEqual(response.json()['Agility'], 20)
        self.assertTrue(response.json()['Constitution'])
        self.assertGreaterEqual(response.json()['Constitution'], 1)
        self.assertLessEqual(response.json()['Constitution'], 20)
        self.assertTrue(response.json()['Stature'])
        self.assertGreaterEqual(response.json()['Stature'], 1)
        self.assertLessEqual(response.json()['Stature'], 20)
        self.assertTrue(response.json()['Intelligence'])
        self.assertGreaterEqual(response.json()['Intelligence'], 1)
        self.assertLessEqual(response.json()['Intelligence'], 20)
        self.assertTrue(response.json()['Education'])
        self.assertGreaterEqual(response.json()['Education'], 1)
        self.assertLessEqual(response.json()['Education'], 20)
        self.assertTrue(response.json()['Total'])
        self.assertGreaterEqual(response.json()['Total'], 6)
        self.assertLessEqual(response.json()['Total'], 120)
        self.assertEqual(response.json()['Total'], 
            response.json()['Fitness'] +
            response.json()['Agility'] +
            response.json()['Constitution'] +
            response.json()['Stature'] +
            response.json()['Intelligence'] +
            response.json()['Education'])


    def test_post_simple_fail_import(self):
        """
        """
        response = self.rpgtools_api_client.post(MODEL_URL,
                                                 ACTION_RUNNER_INPUT_SIMPLE_FAIL_IMPORT,
                                                 format="json")
        self.assertEqual(response.status_code, CODES["created"])
        self.assertTrue(response.json()["foo_bar"]["error"])
        self.assertTrue(response.json()["foo_bar"]["error"]["message"])
        self.assertTrue(response.json()["foo_bar"]["error"]["exception"])