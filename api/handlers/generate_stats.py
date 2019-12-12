# -*- coding: utf-8 -*-
"""
Defines the generate_stats actions
"""
import importlib

def iterate_input(handler_input, additional_input):
    """
    iterate_input
    """
    response = {}
    for stat in handler_input:
        print(stat)
        if not additional_input:
            additional_input = response
        if 'Method' in handler_input[stat]:
            method = handler_input[stat]['Method']
            try:
                module_name = 'api.handlers.'+method
                module = importlib.import_module(module_name)
                response[stat] = module.run(handler_input[stat]['Input'], additional_input)
            except ImportError as import_error:
                response[stat] = 'Failed to find an action method named '+\
                    method+'('+import_error+').'
        else:
            additional_input = response
            response[stat] = iterate_input(handler_input[stat], additional_input)
    return response


def run(handler_input, additional_input=None):
    """
    run
    """
    response = iterate_input(handler_input, additional_input)
    return response
