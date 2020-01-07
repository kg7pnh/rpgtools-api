# -*- coding: utf-8 -*-
"""
Defines the calculation handler
"""
import math # pylint: disable=unused-import
from api.handlers import conditional
from api.handlers import die_roll

OPERATORS = ['+',
             '-',
             '*',
             '/',
             '**',
             '%',
             '(',
             ')',
             '[',
             ']',
             'int',
             'math.trunc',
             'math.ceil']

def run(run_input, additional_input=None):
    """
    run
    """
    result = 0
    formula = ''
    exception = False
    for run_entry in run_input:
        if run_entry == 'formula':
            for formula_entry in run_input['formula']:
                if isinstance(run_input[run_entry][formula_entry], int):
                    formula = formula + str(run_input[run_entry][formula_entry])
                elif run_input[run_entry][formula_entry] in OPERATORS:
                    formula = str(formula) + run_input[run_entry][formula_entry]
                elif isinstance(run_input[run_entry][formula_entry], dict) \
                    and 'die_roll' in run_input['formula'][formula_entry]:
                    value = \
                        die_roll.run(
                            run_input[run_entry][formula_entry]['die_roll']['input'],
                            additional_input)
                    formula = str(formula) + str(value)
                elif isinstance(run_input[run_entry][formula_entry], dict) \
                    and  'conditional' in run_input['formula'][formula_entry]:
                    value = \
                        conditional.run(
                            run_input[run_entry][formula_entry]['conditional']['input'],
                            additional_input)
                    formula = str(formula) + str(value)
                elif not additional_input is None \
                    and run_input[run_entry][formula_entry] in additional_input:
                    formula = str(formula) + \
                        str(additional_input[run_input[run_entry][formula_entry]])
                else:
                    exception = True
                    result = 'Invalid option: "[' + run_entry + '][' + formula_entry + ']"!'
        else:
            exception = True
            result = 'Invalid option: ' + run_entry + '!'

    if not exception:
        result = eval(formula) # pylint: disable=eval-used

    return result
