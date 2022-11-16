# -*- coding: utf-8 -*-
# TODO: update docstring
"""_summary_

"""
from random import randint


def roll(die_size):
    # TODO: update docstring
    """_summary_

    Args:
        die_size (_type_): _description_

    Returns:
        _type_: _description_
    """
    return randint(1, die_size)


def process_modifier(value,
                     modifier,
                     modification):
    # TODO: update docstring
    """_summary_

    Args:
        value (_type_): _description_
        modifier (_type_): _description_
        modification (_type_): _description_

    Returns:
        _type_: _description_
    """
    result = value
    if modification == '+':
        result = result + modifier
    if modification == '-':
        result = result - modifier
    if modification == '*':
        result = result * modifier
    if modification == '/':
        result = result / modifier
    return int(result)


def run_roll(run_input):
    # TODO: update docstring
    """_summary_

    Args:
        run_input (_type_): _description_

    Returns:
        _type_: _description_
    """
    count = 0
    die_roll = 0
    result = 0
    while count < run_input['die_count']:
        count += 1
        die_roll = roll(run_input['die_size'])

        # if a per roll modifier is specified, apply it
        if 'per_modifier' in run_input and not run_input['per_modifier'] is None:
            die_roll = process_modifier(die_roll,
                                        run_input['per_modifier']['value'],
                                        run_input['per_modifier']['mod_type'])
        result = result + die_roll

    # if a roll modifier is specified, apply it
    if 'roll_modifier' in run_input and not run_input['roll_modifier'] is None:
        result = process_modifier(result,
                                  run_input['roll_modifier']['value'],
                                  run_input['roll_modifier']['mod_type'])

    # if a post roll modifier is specified, apply it
    if 'post_modifier' in run_input and not run_input['post_modifier'] is None:
        result = process_modifier(result,
                                  run_input['post_modifier']['value'],
                                  run_input['post_modifier']['mod_type'])

    return result


def run_condition(run_input):
    # TODO: update docstring
    """_summary_

    Args:
        run_input (_type_): _description_

    Returns:
        _type_: _description_
    """
    roll_result = 0
    if run_input['reroll']['condition'] == '==':
        roll_result = run_roll(run_input)
        while roll_result == run_input['reroll']['value']:
            roll_result = run_roll(run_input)
    if run_input['reroll']['condition'] == '<=':
        roll_result = run_roll(run_input)
        while roll_result <= run_input['reroll']['value']:
            roll_result = run_roll(run_input)
    if run_input['reroll']['condition'] == '<':
        roll_result = run_roll(run_input)
        while roll_result < run_input['reroll']['value']:
            roll_result = run_roll(run_input)
    if run_input['reroll']['condition'] == '>=':
        roll_result = run_roll(run_input)
        while roll_result >= run_input['reroll']['value']:
            roll_result = run_roll(run_input)
    if run_input['reroll']['condition'] == '>':
        roll_result = run_roll(run_input)
        while roll_result > run_input['reroll']['value']:
            roll_result = run_roll(run_input)
    return roll_result


def run(run_input, additional_input=None):
    # TODO: update docstring
    """_summary_

    Args:
        run_input (_type_): _description_
        additional_input (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    roll_result = 0

    if not isinstance(run_input['die_size'], int):
        die_size = run_input['die_size']
        run_input['die_size'] = additional_input[die_size]

    if not isinstance(run_input['die_count'], int):
        die_count = run_input['die_count']
        run_input['die_count'] = additional_input[die_count]

    if 'per_modifier' in run_input and not run_input['per_modifier'] is None:
        if 'value' in run_input['per_modifier'] \
                and not isinstance(run_input['per_modifier']['value'], int):
            value = run_input['per_modifier']['value']
            run_input['per_modifier']['value'] = additional_input[value]

    if 'roll_modifier' in run_input and not run_input['roll_modifier'] is None:
        if 'value' in run_input['roll_modifier'] \
                and not isinstance(run_input['roll_modifier']['value'], int):
            value = run_input['roll_modifier']['value']
            run_input['roll_modifier']['value'] = additional_input[value]

    if 'post_modifier' in run_input and not run_input['post_modifier'] is None:
        if 'value' in run_input['post_modifier'] \
                and not isinstance(run_input['post_modifier']['value'], int):
            value = run_input['post_modifier']['value']
            run_input['post_modifier']['value'] = additional_input[value]

    if run_input['die_size'] > 0 and run_input['die_count'] > 0:
        if 'reroll' in run_input and not run_input['reroll'] is None:
            roll_result = run_condition(run_input)
        else:
            roll_result = run_roll(run_input)

    # return the result
    return roll_result
