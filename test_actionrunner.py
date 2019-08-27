import datetime
import json
import requests
import signal
import sys

BASE_URL = 'http://127.0.0.1:8000/api/v1'
ACTION_RUNNER_INPUT = {
    "action_input": {
        "Fitness": {
            "Method": "die-roll",
            "Input": {
                "die_size": 6,
                "die_count": 4,
                "roll_modifier_type": "-",
                "roll_modifier_value": 4,
                "reroll_condition": "==",
                "reroll_value": 0
            }
        },
        "Agility": {
            "Method": "die-roll",
            "Input": {
                "die_size": 6,
                "die_count": 4,
                "roll_modifier_type": "-",
                "roll_modifier_value": 4,
                "reroll_condition": "==",
                "reroll_value": 0
            }
        },
        "Constitution": {
            "Method": "die-roll",
            "Input": {
                "die_size": 6,
                "die_count": 4,
                "roll_modifier_type": "-",
                "roll_modifier_value": 4,
                "reroll_condition": "==",
                "reroll_value": 0
            }
        },
        "Stature": {
            "Method": "die-roll",
            "Input": {
                "die_size": 6,
                "die_count": 4,
                "roll_modifier_type": "-",
                "roll_modifier_value": 4,
                "reroll_condition": "==",
                "reroll_value": 0
            }
        },
        "Intelligence": {
            "Method": "die-roll",
            "Input": {
                "die_size": 6,
                "die_count": 4,
                "roll_modifier_type": "-",
                "roll_modifier_value": 4,
                "reroll_condition": "==",
                "reroll_value": 0
            }
        },
        "Education": {
            "Method": "die-roll",
            "Input": {
                "die_size": 6,
                "die_count": 4,
                "roll_modifier_type": "-",
                "roll_modifier_value": 4,
                "reroll_condition": "==",
                "reroll_value": 0
            }
        } 
    }
}

SUCCESSFUL_RUNS = 0
START_TIME = datetime.datetime.now()
END_TIME = None

def signal_handler(sig, frame):
    global END_TIME
    END_TIME = datetime.datetime.now()  
    print('Exiting due to user input...')
    print_result()
    sys.exit(0)

def print_result():
    global SUCCESSFUL_RUNS
    global START_TIME
    global END_TIME
    run_time = (END_TIME - START_TIME).total_seconds()
    print('Successfully ran '+str(SUCCESSFUL_RUNS)+' test runs in '+str(run_time)+' seconds.')

def get_token():
    """
    get_token()
    """
    token = None
    url = BASE_URL + '/token'
    headers = {"Content-Type": "application/json"}
    data = { "username": "admin","password": "adminpass"}
    response = requests.post(url, data=json.dumps(data),headers=headers)
    if response.status_code == 200:
        token = response.json()['access']
    return token

def submit_request(token):
    """
    submit_request()
    """
    url = BASE_URL + "/action-runner"
    headers = {"Content-Type": "application/json", "Authorization": "Bearer "+token}
    response = requests.post(url, data=json.dumps(ACTION_RUNNER_INPUT), headers=headers)
    if response.status_code == 200:
        return response.json()

def run_test(token):
    signal.signal(signal.SIGINT, signal_handler)
    global SUCCESSFUL_RUNS
    global END_TIME
    while 1:
        success = True
        response = submit_request(token)
        for item in response:
            if response[item] == 0:
                success = False
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