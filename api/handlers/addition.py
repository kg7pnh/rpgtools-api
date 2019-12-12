# -*- coding: utf-8 -*-
"""
Defines the addition action
"""

def run(run_input, additional_input=None):
    """
    run
    """
    print(run_input)
    print(additional_input)
    total = 0
    for input_entry in run_input:
        print(input_entry)
        if input_entry == 'additional_input':
            for additional_entry in run_input['additional_input']:
                total = total + additional_input[additional_entry]
        else:
            for value in run_input[input_entry]:
                total = total + value
    return total
