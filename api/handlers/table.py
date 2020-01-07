# -*- coding: utf-8 -*-
"""
Defines the table handler
"""

def run(run_input, additional_input=None):
    """
    run
    """
    result = ''
    # style = run_input['style']

    if not isinstance(run_input['choice'], int):
        choice = run_input['choice']
        if not additional_input is None and choice in additional_input:
            run_input['choice'] = additional_input[choice]
        else:
            run_input['choice'] = choice
    else:
        run_input['choice'] = str(run_input['choice'])

    choice = str(run_input['choice'])
    table = run_input['choices']

    if choice in table:
        result = table[choice]
    else:
        result = 'no result matched'
    return result
