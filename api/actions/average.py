# -*- coding: utf-8 -*-
import math
"""
Defines the average actions
"""

def iterate_parameters(input, additional_input):
    """
    iterate_parameters
    """
    response = {}
    print(type(input))
    print(input)
    for entry in input:
        print(entry)
        print(input[entry])
        if isinstance(input[entry], (int, long, float)):
            response[entry] = additional_input[entry]
        else:
            results = iterate_parameters(input, additional_input)
    return response

def run(input, additional_input = None):
    """
    run
    """
    print(input)
    print(additional_input)
    total = 0
    count = 0
    round_down = False
    round_up = False

    for entry in input:
        print(entry)
        if entry == 'Round':
            if input[entry] == "Up":
                round_down = False
                round_up = True
            elif input[entry] == "Down":
                round_down = True
                round_up = False
        elif entry == 'additional_input':
            print(input['additional_input'])
            # for parameter in input['additional_input']:
            values = iterate_parameters(input['additional_input'], additional_input)

            total = total + additional_input[entry]
            count = count + 1
        else:
            for value in input[entry]:
                total = total + value
                count = count + 1
    if round_down:
        result = math.trunc(total / count)
    else:
        result = math.ceil(total / count)
    return result