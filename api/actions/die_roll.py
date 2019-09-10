# -*- coding: utf-8 -*-
"""
Defines the die_roll actions
"""
from random import randint

def roll(die_size):
    """
    roll
    """
    return randint(1,die_size)

def process_modifier(value,
                    modifier,
                    modification):
    """
    process_modifier
    """
    if modification == '+':
        value = value + modifier
    if modification == '-':
        value = value - modifier
    if modification == '*':
        value = value * modifier
    if modification == '/':
        value = value / modifier
    return value

def run_roll(die_size,
             die_count,
             per_modifier_type,
             per_modifier_value,
             roll_modifier_type,
             roll_modifier_value,
             post_modifier_type,
             post_modifier_value):
    """
    run_roll
    """

    count = 0
    die_roll = 0
    result = 0
    while count < die_count:
        count += 1
        die_roll = roll(die_size)

        # if a per roll modifier is specified, apply it
        if per_modifier_type and per_modifier_value:
            die_roll = process_modifier(die_roll, per_modifier_value, per_modifier_type)

        result = result + die_roll

    # if a roll modifier is specified, apply it
    if roll_modifier_type and roll_modifier_value:
        result = process_modifier(result, roll_modifier_value, roll_modifier_type)

    # if a post roll modifier is specified, apply it
    if post_modifier_type and post_modifier_value:
        result = process_modifier(result, post_modifier_value, post_modifier_type)

    return result

def run(input):
    """
    run
    """
    print(input)
    die_size = input['die_size']
    die_count = input['die_count']
    per_modifier_type = None
    per_modifier_value = None
    roll_modifier_type = None
    roll_modifier_value = None
    post_modifier_type = None
    post_modifier_value = None

    if 'per_modifier_type' in input:
        per_modifier_type = input['per_modifier_value']
    if 'per_modifier_value' in input:
        per_modifier_value = input['roll_modifier_value']
    if 'roll_modifier_type' in input:
        roll_modifier_type = input['roll_modifier_type']
    if 'roll_modifier_value' in input:
        roll_modifier_value = input['roll_modifier_value']
    if 'post_modifier_type' in input:
        post_modifier_type = input['post_modifier_type']
    if 'post_modifier_value' in input:
        post_modifier_value = input['post_modifier_value']
    if 'reroll_condition' in input:
        reroll_condition = input['reroll_condition']
    if 'reroll_value' in input:
        reroll_value = input['reroll_value']

    roll_result = 0
    if die_size > 0 and die_count > 0:
        if reroll_condition == '==':
            while roll_result == reroll_value:
                roll_result = run_roll(die_size,
                                       die_count,
                                       per_modifier_type,
                                       per_modifier_value,
                                       roll_modifier_type,
                                       roll_modifier_value,
                                       post_modifier_type,
                                       post_modifier_value)
        elif reroll_condition == '<=':
            while roll_result <= reroll_value:
                roll_result = run_roll(die_size,
                                       die_count,
                                       per_modifier_type,
                                       per_modifier_value,
                                       roll_modifier_type,
                                       roll_modifier_value,
                                       post_modifier_type,
                                       post_modifier_value)
        elif reroll_condition == '<':
            while roll_result < reroll_value:
                roll_result = run_roll(die_size,
                                       die_count,
                                       per_modifier_type,
                                       per_modifier_value,
                                       roll_modifier_type,
                                       roll_modifier_value,
                                       post_modifier_type,
                                       post_modifier_value)
        elif reroll_condition == '>=':
            while roll_result >= reroll_value:
                roll_result = run_roll(die_size,
                                       die_count,
                                       per_modifier_type,
                                       per_modifier_value,
                                       roll_modifier_type,
                                       roll_modifier_value,
                                       post_modifier_type,
                                       post_modifier_value)
        elif reroll_condition == '>':
            while roll_result > reroll_value:
                roll_result = run_roll(die_size,
                                       die_count,
                                       per_modifier_type,
                                       per_modifier_value,
                                       roll_modifier_type,
                                       roll_modifier_value,
                                       post_modifier_type,
                                       post_modifier_value)
        else:
            roll_result = run_roll(die_size,
                                   die_count,
                                   per_modifier_type,
                                   per_modifier_value,
                                   roll_modifier_type,
                                   roll_modifier_value,
                                   post_modifier_type,
                                   post_modifier_value)

    # return the result
    return roll_result