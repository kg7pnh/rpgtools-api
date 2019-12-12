# -*- coding: utf-8 -*-
"""
Defines the addition action
"""

def run(input, additional_input = None):
    """
    run
    """
    print(input)
    print(additional_input)
    total = 0
    for entry in input:
        print(entry)
        if entry == 'additional_input':
            for entry in input['additional_input']:
                total = total + additional_input[entry]
        else:
            for value in input[entry]:
                total = total + value
    return total