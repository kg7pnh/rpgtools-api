# -*- coding: utf-8 -*-
"""
Defines the table handler
"""

def run(run_input, additional_input):
    """
    """
    result = ''
    style = run_input['style']

    if not isinstance(run_input['choice'], int):
        choice = run_input['choice']
        run_input['choice'] = additional_input[choice]
    
        choice = str(run_input['choice'])

    table = run_input['choices']

    if choice in table:
        result = table[choice]

    return result