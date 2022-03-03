# -*- coding: utf-8 -*- # pylint: disable=too-many-lines
"""
Defines test case run against the API for DieRoll model
"""
import math
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
        ATTR_RANGE [Static]: Value range for some of the assertions involving
                             a specific value range.
    """
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
                "name": "BaseCoolness",
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
                "name": "Coolness",
                "method": "conditional",
                "input": {
                    "test_value": "BaseCoolness",
                    "conditions": {
                        "0": {
                            "test": "<=",
                            "eval": 0,
                            "result": 0
                        },
                        "1": {
                            "test": ">",
                            "eval": 0,
                            "result": "BaseCoolness"
                        }
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
    ATTR_RANGE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    def test_run(self):
        """Executes a test against the target url using the defined json package 1000 times."""
        for iteration in range(1000): # pylint: disable=unused-variable
            response = self.rpgtools_api_client.post(MODEL_URL,
                                                     self.JSON_INPUT,
                                                     format="json")
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
            self.assertEqual(response.json()['Military Experience Base'],
                            math.trunc((120 - response.json()['Total']) / 7))
            self.assertGreaterEqual(response.json()['Time In Combat'],
                                    response.json()['Military Experience Base'])
            self.assertLessEqual(response.json()['Time In Combat'],
                                response.json()['Military Experience Base'] * 6)
            self.assertGreaterEqual(response.json()['Coolness'], 0)
            self.assertGreaterEqual(response.json()['RADS'], 6)
            self.assertLessEqual(response.json()['RADS'], response.json()['RADS'] * 6)
            self.assertTrue(isinstance(response.json()['Age'],int))
            self.assertTrue(isinstance(response.json()['Officer'], bool))
            self.assertTrue(isinstance(response.json()['Rank Number'], int))
            self.assertGreaterEqual(response.json()['Rank Number'], -1)
            self.assertLessEqual(response.json()['Rank Number'], 8)
            self.assertTrue(response.json()['Rank'])
