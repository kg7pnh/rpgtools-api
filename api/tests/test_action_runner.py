# -*- coding: utf-8 -*- # pylint: disable=too-many-lines
"""
Defines test case run against the API for DieRoll model
"""
import math
from django.test import tag
from api.tests.base import RPGToolsApiBaseTestCase
from api.tests.base import ADMIN_USER
from api.tests.base import BASE_URL
from api.tests.base import CODES
from api.tests.base import READ_ONLY_USER
from api.tests.base import TOKEN_URL

MODEL_URL = BASE_URL + 'action-runner'

FIXTURES = ['test_users']

ACTION_RUNNER_INPUT_DIEROLL_ADD_INPUT = {
    "action_input": [
        {
            "name": "test_case",
            "method": "die_roll",
            "input": {
                "die_size": "die_size",
                "die_count": "die_count",
                "per_modifier": {
                    "mod_type": "+",
                    "value": "per_value"
                },
                "roll_modifier": {
                    "mod_type": "+",
                    "value": "roll_value"
                },
                "post_modifier": {
                    "mod_type": "*",
                    "value": "post_value"
                }
            }
        }
    ],
    "additional_input": {
        "die_size": 6,
        "die_count": 1,
        "per_value": 1,
        "roll_value": 3,
        "post_value": 10
    }
}

ACTION_RUNNER_INPUT_SIMPLE_SUCCESSFULL = {
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

ACTION_RUNNER_INPUT_LARGE_SUCCESSFULL = {
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

ACTION_RUNNER_INPUT_COMPLEX_SUCCESSFULL = {
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
        },
        {
            "name": "Total",
            "method": "calculation",
            "input": {
                "formula": {
                    "0": "int",
                    "1": "(",
                    "2": "Fitness",
                    "3": "+",
                    "4": "Agility",
                    "5": "+",
                    "6": "Constitution",
                    "7": "+",
                    "8": "Stature",
                    "9": "+",
                    "10": "Intelligence",
                    "11": "+",
                    "12": "Education",
                    "13": ")"
                }
            }
        },
        {
            "name": "Strength",
            "method": "calculation",
            "input": {
                "formula": {
                    "0": "math.trunc",
                    "1": "(",
                    "2": "(",
                    "3": "Fitness",
                    "4": "+",
                    "5": "Stature",
                    "6": ")",
                    "7": "/",
                    "8": 2,
                    "9": ")"
                }
            }
        },
        {
            "name": "Hit Capacity - Head",
            "method": "calculation",
            "input": {
                "formula": {
                    "0": "Constitution"
                }
            }
        },
        {
            "name": "Hit Capacity - Chest",
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
        {
            "name": "Hit Capacity - Other",
            "method": "calculation",
            "input": {
                "formula": {
                    "0": "Constitution",
                    "1": "+",
                    "2": "Stature"
                }
            }
        },
        {
            "name": "Weight",
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
        {
            "name": "Load",
            "method": "calculation",
            "input": {
                "formula": {
                    "0": "(",
                    "1": "Strength",
                    "2": "*",
                    "3": 2,
                    "4": ")",
                    "5": "+",
                    "6": "Constitution"
                }
            }
        },
        {
            "name": "Throw Range",
            "method": "calculation",
            "input": {
                "formula": {
                    "0": "Strength",
                    "1": "*",
                    "2": 2
                }
            }
        },
        {
            "name": "Military Experience Base",
            "method": "calculation",
            "input": {
                "formula": {
                    "0": "math.trunc",
                    "1": "(",
                    "2": "(",
                    "3": 120,
                    "4": "-",
                    "5": "Total",
                    "6": ")",
                    "7": "/",
                    "8": 7,
                    "9": ")"
                }
            }
        },
        {
            "name": "Time In Combat",
            "method": "die_roll",
            "input": {
                "die_size": 6,
                "die_count": "Military Experience Base"
            }
        },
        {
            "name": "Coolness",
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
        {
            "name": "RADS",
            "method": "die_roll",
            "input": {
                "die_size": 6,
                "die_count": "Military Experience Base"
            }
        },
        {
            "name": "Age",
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
        {
            "name": "Officer",
            "method": "conditional",
            "input": {
                "test_value": {
                    "die_roll": {
                        "input": {
                            "die_size": 6,
                            "die_count": 1,
                            "roll_modifier": {
                                "mod_type": "+",
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
        {
            "name": "Rank Number",
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
                                    "1": {
                                        "test": "==",
                                        "eval": 1,
                                        "result": -1
                                    },
                                    "2": {
                                        "test": "==",
                                        "eval": 2,
                                        "result": -1
                                    },
                                    "3": {
                                        "test": "==",
                                        "eval": 3,
                                        "result": 0
                                    },
                                    "4": {
                                        "test": "==",
                                        "eval": 4,
                                        "result": 0
                                    },
                                    "5": {
                                        "test": "==",
                                        "eval": 5,
                                        "result": 1
                                    },
                                    "6": {
                                        "test": "==",
                                        "eval": 6,
                                        "result": 1
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        {
            "name": "Rank",
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
    ]
}

ACTION_RUNNER_INPUT_SIMPLE_FAIL_IMPORT = {
    "action_input": [
        {
            "name": "test_case",
            "method": "foo_bar",
            "input": {
                "foo": "bar"
            }
        }
    ]
}

ACTION_RUNNER_INPUT_BAD_CALCULATION_NO_FORMULA = {
    "action_input": [
        {
            "name": "test_case",
            "method": "calculation",
            "input": {
                "test": "fail"
            }
        }
    ]
}

ACTION_RUNNER_INPUT_BAD_CALCULATION_BAD_FORMULA = {
    "action_input": [
        {
            "name": "test_case",
            "method": "calculation",
            "input": {
                "formula": {
                    "0": 3,
                    "1": "fail"
                }
            }
        }
    ],
    "additional_input": {
        "test": 5
    }
}

ACTION_RUNNER_TABLE_NORESULT = {
    "action_input": [
        {
            "name": "test_case",
            "method": "table",
            "input": {
                "style": "simple",
                "choice": 12,
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

ACTION_RUNNER_TABLE_STRING_CHOICE = {
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

ACTION_RUNNER_NO_METHOD = {
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

ACTION_RUNNER_AVG_NOINPUT = {
    "action_input": [
        {
            "name": "test_case",
            "method": "average",
            "input": {
            }
        }
    ]
}

ACTION_RUNNER_AVG_NOADDINPUT_NO_ROUND = {
    "action_input": [
        {
            "name": "test_case",
            "method": "average",
            "input": {
                "0": 100,
                "1": 51,
                "2": 12
            }
        }
    ]
}

ACTION_RUNNER_AVG_NOADDINPUT_ROUND_DOWN = {
    "action_input": [
        {
            "name": "test_case",
            "method": "average",
            "input": {
                "round": "down",
                "0": 100,
                "1": 51,
                "2": 12
            }
        }
    ]
}

ACTION_RUNNER_AVG_NOADDINPUT_ROUND_UP = {
    "action_input": [
        {
            "name": "test_case",
            "method": "average",
            "input": {
                "round": "up",
                "0": 100,
                "1": 51,
                "2": 12
            }
        }
    ]
}

ACTION_RUNNER_AVG_NOADDINPUT_ROUND_DROP = {
    "action_input": [
        {
            "name": "test_case",
            "method": "average",
            "input": {
                "round": "drop",
                "0": 100,
                "1": 51,
                "2": 12
            }
        }
    ]
}

ACTION_RUNNER_AVG_ADDINPUT_ROUND_DROP = {
    "action_input": [
        {
            "name": "test_case",
            "method": "average",
            "input": {
                "round": "drop",
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

ACTION_RUNNER_AVG_ADDINPUT_INVALID = {
    "action_input": [
        {
            "name": "test_case",
            "method": "average",
            "input": {
                "round": "drop",
                "0": 100,
                "1": 51,
                "2": 12,
                "3": "test",
                "4": "test_2",
                "5": "test_1"
            }
        }
    ],
    "additional_input": {
        "test_1": 5,
        "test_2": 6
    }
}

ACTION_RUNNER_CON_COMPARE_INT_TRUE = {
    "action_input": [
        {
            "name": "test_case",
            "method": "conditional",
            "input": {
                "test_value": 10,
                "conditions": {
                    "0": {
                        "test": ">=",
                        "eval": 70,
                        "result": False
                    },
                    "1": {
                        "test": "<",
                        "eval": 70,
                        "result": True
                    }
                }
            }
        }
    ]
}

ACTION_RUNNER_CON_COMPARE_INT_ADDINPUT_TRUE = {
    "action_input": [
        {
            "name": "test_case",
            "method": "conditional",
            "input": {
                "test_value": 10,
                "conditions": {
                    "0": {
                        "test": ">=",
                        "eval": "test",
                        "result": False
                    },
                    "1": {
                        "test": "<",
                        "eval": "test",
                        "result": True
                    }
                }
            }
        }
    ],
    "additional_input": {
        "test": 0
    }
}

ACTION_RUNNER_CON_CONDITIONAL_BAD_OPERATOR = {
    "action_input": [
        {
            "name": "test_case",
            "method": "conditional",
            "input": {
                "test_value": 10,
                "conditions": {
                    "0": {
                        "test": "f",
                        "eval": 70,
                        "result": False
                    },
                    "1": {
                        "test": "f",
                        "eval": 70,
                        "result": True
                    }
                }
            }
        }
    ]
}

ACTION_RUNNER_CON_NESTED_CON = {
    "action_input": [
        {
            "name": "test_case",
            "method": "conditional",
            "input": {
                "test_value": 10,
                "conditions": {
                    "0": {
                        "test": ">=",
                        "eval": 70,
                        "result": False
                    },
                    "1": {
                        "test": "<",
                        "eval": 70,
                        "result": {
                            "conditional": {
                                "input": {
                                    "test_value": 10,
                                    "conditions": {
                                        "0": {
                                            "test": ">=",
                                            "eval": 33,
                                            "result": False
                                        },
                                        "1": {
                                            "test": "<",
                                            "eval": 33,
                                            "result": True
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    ]
}

ACTION_RUNNER_CON_NESTED_BAD_OPTION = {
    "action_input":  [
        {
            "name": "test_case",
            "method": "conditional",
            "input": {
                "test_value": 10,
                "conditions": {
                    "0": {
                        "test": ">=",
                        "eval": 70,
                        "result": False
                    },
                    "1": {
                        "test": "<",
                        "eval": 70,
                        "result": {
                            "fudge": {
                                "input": {
                                    "test_value": 10,
                                    "conditions": {
                                        "0": {
                                            "test": ">=",
                                            "eval": 33,
                                            "result": False
                                        },
                                        "1": {
                                            "test": "<",
                                            "eval": 33,
                                            "result": True
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    ]
}

ACTION_RUNNER_INPUT_SIMPLE_CON_RSLT_ADD_INPUT = {
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

ACTION_RUNNER_INPUT_CON_RESULT_STR = {
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
    ]
}

@tag("action_runner_admin")
class TestAdmin(RPGToolsApiBaseTestCase):
    """
    TestAdmin
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
    TestReadOnly
    """
    fixtures = FIXTURES
    token = RPGToolsApiBaseTestCase.rpgtools_api_client.post(TOKEN_URL,
                                                             READ_ONLY_USER,
                                                             format="json").json()["access"]

    def test_post_success(self):
        """
        test_post_success
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
class TestAnonymous(RPGToolsApiBaseTestCase): #pylint: disable=too-many-public-methods
    """
    TestAnonymous
    """

    def test_post_simple_success(self):
        """
        test_post_simple_success
        """
        for iteration in range(1000): # pylint: disable=unused-variable
            response = self.rpgtools_api_client.post(MODEL_URL,
                                                     ACTION_RUNNER_INPUT_SIMPLE_SUCCESSFULL,
                                                     format="json")
            self.assertEqual(response.status_code, CODES["created"])
            self.assertGreaterEqual(response.json()['test_case'], 1)
            self.assertLessEqual(response.json()['test_case'], 20)

    def test_post_large_success(self):
        """
        test_post_large_success
        """
        for iteration in range(1000): # pylint: disable=unused-variable
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
        test_post_complex_success
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
        self.assertTrue(response.json()['Strength'])
        self.assertEqual(response.json()['Strength'],
                         int((response.json()['Fitness'] +
                             response.json()['Stature']) / 2))
        self.assertTrue(response.json()['Hit Capacity - Head'])
        self.assertEqual(response.json()['Hit Capacity - Head'],
                         response.json()['Constitution'])
        self.assertTrue(response.json()['Hit Capacity - Chest'])
        self.assertEqual(response.json()['Hit Capacity - Chest'],
                         response.json()['Strength'] +
                         response.json()['Constitution'] +
                         response.json()['Stature'])
        self.assertTrue(response.json()['Hit Capacity - Other'])
        self.assertEqual(response.json()['Hit Capacity - Other'],
                         response.json()['Constitution'] +
                         response.json()['Stature'])
        self.assertTrue(response.json()['Weight'])
        self.assertEqual(response.json()['Weight'],
                         response.json()['Stature'] * 4 + 40)
        self.assertTrue(response.json()['Load'])
        self.assertEqual(response.json()['Load'],
                         (response.json()['Strength'] * 2) +
                         response.json()['Constitution'])
        self.assertTrue(response.json()['Throw Range'])
        self.assertEqual(response.json()['Throw Range'],
                         response.json()['Strength'] * 2)
        self.assertEqual(response.json()['Military Experience Base'], math.trunc((120 - response.json()['Total']) / 7))
        self.assertGreaterEqual(response.json()['Time In Combat'], response.json()['Military Experience Base'])
        self.assertLessEqual(response.json()['Time In Combat'], response.json()['Military Experience Base'] * 6)
        self.assertGreaterEqual(response.json()['Coolness'], 0)
        self.assertGreaterEqual(response.json()['RADS'], 6)
        self.assertLessEqual(response.json()['RADS'], response.json()['RADS'] * 6)
        self.assertTrue(isinstance(response.json()['Age'],int))
        self.assertTrue(isinstance(response.json()['Officer'], bool))
        self.assertTrue(isinstance(response.json()['Rank Number'], int))
        self.assertGreaterEqual(response.json()['Rank Number'], -1)
        self.assertLessEqual(response.json()['Rank Number'], 8)
        self.assertTrue(response.json()['Rank'])

    def test_post_simple_fail_import(self):
        """
        test_post_simple_fail_import
        """
        response = self.rpgtools_api_client.post(MODEL_URL,
                                                 ACTION_RUNNER_INPUT_SIMPLE_FAIL_IMPORT,
                                                 format="json")
        self.assertEqual(response.status_code, CODES["created"])
        self.assertTrue(response.json()["test_case"])
        self.assertTrue(response.json()["test_case"]["error"]["message"])
        self.assertTrue(response.json()["test_case"]["error"]["exception"])

    def test_post_calculation_fail_no_formula(self):
        """
        test_post_calculation_fail_no_formula
        """
        response = self.rpgtools_api_client.post(MODEL_URL,
                                                 ACTION_RUNNER_INPUT_BAD_CALCULATION_NO_FORMULA,
                                                 format="json")
        self.assertEqual(response.status_code, CODES["created"])
        self.assertTrue(response.json()["test_case"], "Invalid option: test!")

    def test_post_calculation_fail_bad_formula(self):
        """
        test_post_calculation_fail_bad_formula
        """
        response = self.rpgtools_api_client.post(MODEL_URL,
                                                 ACTION_RUNNER_INPUT_BAD_CALCULATION_BAD_FORMULA,
                                                 format="json")
        self.assertEqual(response.status_code, CODES["created"])
        self.assertTrue(response.json()["test_case"], "Invalid option \"[formula][1]\"!")

    def test_post_dieroll_add_input(self):
        """
        test_post_dieroll_add_input
        """
        response = self.rpgtools_api_client.post(MODEL_URL,
                                                 ACTION_RUNNER_INPUT_DIEROLL_ADD_INPUT,
                                                 format="json")
        self.assertEqual(response.status_code, CODES["created"])
        self.assertGreaterEqual(response.json()["test_case"], 50)
        self.assertLessEqual(response.json()["test_case"], 100)

    def test_post_table_noresult(self):
        """
        test_post_table_noresult
        """
        response = self.rpgtools_api_client.post(MODEL_URL,
                                                 ACTION_RUNNER_TABLE_NORESULT,
                                                 format="json")
        self.assertEqual(response.status_code, CODES["created"])
        self.assertEqual(response.json()["test_case"], "no result matched")

    def test_post_table_string_choice(self):
        """
        test_post_table_string_choice
        """
        response = self.rpgtools_api_client.post(MODEL_URL,
                                                 ACTION_RUNNER_TABLE_STRING_CHOICE,
                                                 format="json")
        self.assertEqual(response.status_code, CODES["created"])
        self.assertEqual(response.json()["test_case"], "Major")

    def test_post_no_method(self):
        """
        test_post_no_method
        """
        response = self.rpgtools_api_client.post(MODEL_URL,
                                                 ACTION_RUNNER_NO_METHOD,
                                                 format="json")
        self.assertEqual(response.status_code, CODES["created"])
        self.assertEqual(response.json()["error_entry_index_0"],
            "Action Input entries require \"name\", \"method\""\
            " and \"input\" items to be processed.")

    def test_post_avg_noinput(self):
        """
        test_post_avg_noinput
        """
        response = self.rpgtools_api_client.post(MODEL_URL,
                                                 ACTION_RUNNER_AVG_NOINPUT,
                                                 format="json")
        self.assertEqual(response.status_code, CODES["created"])
        self.assertEqual(response.json()["test_case"], "Incomplete Request: No input provided!")

    def test_post_avg_noaddinput_no_round(self):
        """
        test_post_avg_noaddinput_no_round
        """
        response = self.rpgtools_api_client.post(MODEL_URL,
                                                 ACTION_RUNNER_AVG_NOADDINPUT_NO_ROUND,
                                                 format="json")
        self.assertEqual(response.status_code, CODES["created"])
        self.assertEqual(response.json()["test_case"], 54.333333333333336)

    def test_post_avg_noaddinput_round_down(self):
        """
        test_post_avg_noaddinput_round_down
        """
        response = self.rpgtools_api_client.post(MODEL_URL,
                                                 ACTION_RUNNER_AVG_NOADDINPUT_ROUND_DOWN,
                                                 format="json")
        self.assertEqual(response.status_code, CODES["created"])
        self.assertEqual(response.json()["test_case"], 54)

    def test_post_avg_noaddinput_round_up(self):
        """
        test_post_avg_noaddinput_round_up
        """
        response = self.rpgtools_api_client.post(MODEL_URL,
                                                 ACTION_RUNNER_AVG_NOADDINPUT_ROUND_UP,
                                                 format="json")
        self.assertEqual(response.status_code, CODES["created"])
        self.assertEqual(response.json()["test_case"], 55)

    def test_post_avg_noaddinput_round_drop(self):
        """
        test_post_avg_noaddinput_round_drop
        """
        response = self.rpgtools_api_client.post(MODEL_URL,
                                                 ACTION_RUNNER_AVG_NOADDINPUT_ROUND_DROP,
                                                 format="json")
        self.assertEqual(response.status_code, CODES["created"])
        self.assertEqual(response.json()["test_case"], 54)

    def test_post_avg_addinput_round_drop(self):
        """
        test_post_avg_addinput_round_drop
        """
        response = self.rpgtools_api_client.post(MODEL_URL,
                                                 ACTION_RUNNER_AVG_ADDINPUT_ROUND_DROP,
                                                 format="json")
        self.assertEqual(response.status_code, CODES["created"])
        self.assertEqual(response.json()["test_case"], 34)

    def test_post_avg_addinput_invalid(self):
        """
        test_post_avg_addinput_invalid
        """
        response = self.rpgtools_api_client.post(MODEL_URL,
                                                 ACTION_RUNNER_AVG_ADDINPUT_INVALID,
                                                 format="json")
        self.assertEqual(response.status_code, CODES["created"])
        self.assertEqual(response.json()["test_case"],
                         'Invalid Input(s): additional_input["test"]')

    def test_post_conditional_int_true(self):
        """
        test_post_conditional_int_true
        """
        response = self.rpgtools_api_client.post(MODEL_URL,
                                                 ACTION_RUNNER_CON_COMPARE_INT_TRUE,
                                                 format="json")
        self.assertEqual(response.status_code, CODES["created"])
        self.assertEqual(response.json()["test_case"], True)

    def test_post_conditional_int_addinput_true(self):
        """
        test_post_conditional_int_addinput_true
        """
        response = self.rpgtools_api_client.post(MODEL_URL,
                                                 ACTION_RUNNER_CON_COMPARE_INT_ADDINPUT_TRUE,
                                                 format="json")
        self.assertEqual(response.status_code, CODES["created"])
        self.assertEqual(response.json()["test_case"], False)

    def test_post_conditional_bad_operator(self):
        """
        test_post_conditional_bad_operator
        """
        response = self.rpgtools_api_client.post(MODEL_URL,
                                                 ACTION_RUNNER_CON_CONDITIONAL_BAD_OPERATOR,
                                                 format="json")
        self.assertEqual(response.status_code, CODES["created"])
        self.assertEqual(response.json()["test_case"],
                         'Invalid Operator: "f"!')

    def test_post_conditional_netsed_conditional(self):
        """
        test_post_conditional_netsed_conditional
        """
        response = self.rpgtools_api_client.post(MODEL_URL,
                                                 ACTION_RUNNER_CON_NESTED_CON,
                                                 format="json")
        self.assertEqual(response.status_code, CODES["created"])
        self.assertEqual(response.json()["test_case"], True)

    def test_post_conditional_netsed_bad_option(self):
        """
        test_post_conditional_netsed_conditional
        """
        response = self.rpgtools_api_client.post(MODEL_URL,
                                                 ACTION_RUNNER_CON_NESTED_BAD_OPTION,
                                                 format="json")
        self.assertEqual(response.status_code, CODES["created"])
        self.assertEqual(response.json()["test_case"],
                         'Invalid Method Option: "fudge"!')

    def test_post_conditional_result_additionalinput(self):
        """
        test_post_conditional_result_additionalinput
        """
        for iteration in range(1000): # pylint: disable=unused-variable
            response = self.rpgtools_api_client.post(MODEL_URL,
                                                     ACTION_RUNNER_INPUT_SIMPLE_CON_RSLT_ADD_INPUT,
                                                     format="json")
            self.assertEqual(response.status_code, CODES["created"])
            self.assertEqual(response.json()['test_case'], 0)

    def test_post_conditional_restult_string(self):
        """
        test_post_conditional_restult_string
        """
        for iteration in range(1000): # pylint: disable=unused-variable
            response = self.rpgtools_api_client.post(MODEL_URL,
                                                     ACTION_RUNNER_INPUT_CON_RESULT_STR,
                                                     format="json")
            self.assertEqual(response.status_code, CODES["created"])
            self.assertEqual(response.json()['test_case'], "test")
