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
             per_modifier,
             roll_modifier,
             post_modifier):
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
        if per_modifier:
            die_roll = process_modifier(die_roll, per_modifier["value"], per_modifier["type"])

        result = result + die_roll

    # if a roll modifier is specified, apply it
    if roll_modifier:
        result = process_modifier(result, roll_modifier["value"], roll_modifier["type"])

    # if a post roll modifier is specified, apply it
    if post_modifier:
        result = process_modifier(result, post_modifier["value"], post_modifier["type"])

    return result

def run(input, additional_input = None):
    """
    run
    """
    die_size = input['die_size']
    die_count = input['die_count']
    per_modifier = None
    roll_modifier = None
    post_modifier = None

    if 'per_modifier' in input:
        per_modifier = input['per_modifier']
    if 'roll_modifier' in input:
        roll_modifier = input['roll_modifier']
    if 'post_modifier' in input:
        post_modifier = input['post_modifier']
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
                                       per_modifier,
                                       roll_modifier,
                                       post_modifier)
        elif reroll_condition == '<=':
            while roll_result <= reroll_value:
                roll_result = run_roll(die_size,
                                       die_count,
                                       per_modifier,
                                       roll_modifier,
                                       post_modifier)
        elif reroll_condition == '<':
            while roll_result < reroll_value:
                roll_result = run_roll(die_size,
                                       die_count,
                                       per_modifier,
                                       roll_modifier,
                                       post_modifier)
        elif reroll_condition == '>=':
            while roll_result >= reroll_value:
                roll_result = run_roll(die_size,
                                       die_count,
                                       per_modifier,
                                       roll_modifier,
                                       post_modifier)
        elif reroll_condition == '>':
            while roll_result > reroll_value:
                roll_result = run_roll(die_size,
                                       die_count,
                                       per_modifier,
                                       roll_modifier,
                                       post_modifier)
        else:
            roll_result = run_roll(die_size,
                                       die_count,
                                       per_modifier,
                                       roll_modifier,
                                       post_modifier)

    # return the result
    return roll_result