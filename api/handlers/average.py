# -*- coding: utf-8 -*-
# TODO: update docstring
"""_summary_

Returns:
    _type_: _description_
"""
import math


def get_average(round_method, total, count):
    # TODO: update docstring
    """_summary_

    Args:
        round_method (_type_): _description_
        total (_type_): _description_
        count (_type_): _description_

    Returns:
        _type_: _description_
    """
    if round_method == 'down':
        result = math.trunc(total / count)
    elif round_method == 'up':
        result = math.ceil(total / count)
    elif round_method == 'drop':
        result = int(total / count)
    else:
        result = total / count
    return result


def run(run_input, additional_input=None):
    # TODO: update docstring
    """_summary_

    Args:
        run_input (_type_): _description_
        additional_input (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    total = 0
    count = 0
    round_method = None
    move_on = True
    result = ''

    if not run_input == {}:
        for entry in run_input:
            if entry == 'round':
                round_method = run_input[entry]
            elif isinstance(run_input[entry], int):
                total = total + run_input[entry]
                count = count + 1
            elif run_input[entry] in additional_input:
                total = total + additional_input[run_input[entry]]
                count = count + 1
            else:
                result = result + \
                    'additional_input["' + run_input[entry] + '"]; '
                move_on = False
        if move_on:
            result = get_average(round_method, total, count)
        else:
            result = "Invalid Input(s): " + result[:-2]
    else:
        result = 'Incomplete Request: No input provided!'
    return result
