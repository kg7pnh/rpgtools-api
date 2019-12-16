# -*- coding: utf-8 -*-
"""
Defines the die_roll actions
"""
import importlib

def iterate_input(run_input, additional_input):
    """
    iterate_input
    """
    response = {}
    for stat in run_input:
        print(stat)
        if not additional_input:
            additional_input = response
        if 'Method' in run_input[stat]:
            method = run_input[stat]['Method']
            try:
                module_name = 'api.handlers.'+method
                module = importlib.import_module(module_name)
                response[stat] = module.run(run_input[stat]['Input'], additional_input)
            except ImportError as error:
                response[stat] = '"Failed to find an action method named '+method+' ('+error+'+)."'
        else:
            additional_input = response
            response[stat] = iterate_input(run_input[stat], additional_input)
    return response


def run(run_input, additional_input=None):
    """
    run
    """
    response = iterate_input(run_input, additional_input)
    return response
