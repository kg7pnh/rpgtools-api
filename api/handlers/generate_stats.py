# -*- coding: utf-8 -*-
"""
Defines the die_roll actions
"""
import importlib
import json

def iterate_input(input, additional_input):
    """
    iterate_input
    """
    response = {}
    for stat in input:
        print(stat)
        if not additional_input:
            additional_input = response
        if 'Method' in input[stat]:
            method = input[stat]['Method']
            try:
                module_name = 'api.handlers.'+method
                module = importlib.import_module(module_name)
                response[stat] = module.run(input[stat]['Input'], additional_input)
            except ImportError as error:
                response[stat] = '"Failed to find an action method named '+method+'."'
        else:
            additional_input = response
            response[stat] = iterate_input(input[stat], additional_input)
    return response


def run(input, additional_input = None):
    """
    run
    """
    response = iterate_input(input, additional_input)
    return response
