# -*- coding: utf-8 -*-
"""
Defines the average actions
"""
import math

def iterate_parameters(iterate_input, additional_input):
    """
    iterate_parameters
    """
    response = {}
    print(type(iterate_input))
    print(iterate_input)
    for entry in iterate_input:
        print(entry)
        print(iterate_input[entry])
        if isinstance(iterate_input[entry], (int, float)):
            response[entry] = additional_input[entry]
        else:
            results = iterate_parameters(iterate_input, additional_input)
            print(results)
    return response

def run(run_input, additional_input=None):
    """
    run
    """
    print(run_input)
    print(additional_input)
    total = 0
    count = 0
    round_down = False
    round_up = False

    for entry in run_input:
        print(entry)
        if entry == 'Round':
            if run_input[entry] == "Up":
                round_down = False
                round_up = True
            elif run_input[entry] == "Down":
                round_down = True
                round_up = False
        elif entry == 'additional_input':
            print(run_input['additional_input'])
            # for parameter in input['additional_input']:
            values = iterate_parameters(run_input['additional_input'], additional_input)
            print(values)
            total = total + additional_input[entry]
            count = count + 1
        else:
            for value in run_input[entry]:
                total = total + value
                count = count + 1
    if round_down:
        result = math.trunc(total / count)
    elif round_up:
        result = math.ceil(total / count)
    else:
        result = int(total / count)
    return result
