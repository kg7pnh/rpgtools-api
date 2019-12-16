"""
test_actionrunner.py
executes a number of actionrunner calls to test performance
over time
"""
import datetime
import json
import signal
import sys
import requests

BASE_URL = 'http://127.0.0.1:8000/api/v1'
ACTION_RUNNER_INPUT = {
    "action_input": {
        "Fitness": {
            "Method": "die_roll",
            "Input": {
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
            "Method": "die_roll",
            "Input": {
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
            "Method": "die_roll",
            "Input": {
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
            "Method": "die_roll",
            "Input": {
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
            "Method": "die_roll",
            "Input": {
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
            "Method": "die_roll",
            "Input": {
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

SUCCESSFUL_RUNS = 0
START_TIME = datetime.datetime.now()
END_TIME = None

def signal_handler(sig, frame): # pylint: disable=unused-argument
    """
    signal_handler
    handles [CTRL]+C so script exits gracefully
    """
    global END_TIME # pylint: disable=global-statement
    END_TIME = datetime.datetime.now()
    print('Exiting due to user input...')
    print_result()
    sys.exit(0)

def print_result():
    """
    print_result
    prints result of test to console
    """
    global SUCCESSFUL_RUNS # pylint: disable=global-statement
    global START_TIME # pylint: disable=global-statement
    global END_TIME # pylint: disable=global-statement
    run_time = (END_TIME - START_TIME).total_seconds()
    print('Successfully ran '+str(SUCCESSFUL_RUNS)+' test runs in '+str(run_time)+' seconds.')

def get_token():
    """
    get_token()
    retrieves authoriztion token from api
    """
    token = None
    url = BASE_URL + '/token'
    headers = {"Content-Type": "application/json"}
    data = {"username": "admin", "password": "adminpass"}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        token = response.json()['access']
    return token

def submit_request(token):
    """
    submit_request()
    """
    data = None
    url = BASE_URL + "/action-runner"
    headers = {"Content-Type": "application/json", "Authorization": "Bearer "+token}
    response = requests.post(url, data=json.dumps(ACTION_RUNNER_INPUT), headers=headers)
    if response.status_code == 201:
        data = response.json()
    return data

def run_test(token):
    """
    run_test
    """
    signal.signal(signal.SIGINT, signal_handler)
    global SUCCESSFUL_RUNS # pylint: disable=global-statement
    global END_TIME # pylint: disable=global-statement
    while 1:
        response = submit_request(token)
        print(response)
        for item in response:
            if response[item] == 0:
                print('failed on '+item)
                print('Exiting due to failed test...')
                END_TIME = datetime.datetime.now()
                break
        SUCCESSFUL_RUNS = SUCCESSFUL_RUNS + 1

def main():
    """
    Entry point
    """
    token = get_token()
    if token:
        run_test(token)
    else:
        print('Unable to retrieve token...aborting!')
    print_result()

if __name__ == '__main__':
    main()
