# -*- coding: utf-8 -*-
# TODO: update docstring
"""_summary_

Returns:
    _type_: _description_
"""
import math  # pylint: disable=unused-import
from api.handlers import conditional  # pylint: disable=cyclic-import
from api.handlers import die_roll
from api.handlers import eval_expression

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
             'trunc',
             'ceil']


def get_formula_entry(formula_entry, additional_input):
    # TODO: update docstring
    """_summary_

    Args:
        formula_entry (_type_): _description_
        additional_input (_type_): _description_

    Returns:
        _type_: _description_
    """
    value = None
    exception = False
    if isinstance(formula_entry, int):
        value = str(formula_entry)
    elif formula_entry in OPERATORS:
        value = formula_entry
    elif isinstance(formula_entry, dict) \
            and 'die_roll' in formula_entry:
        value = \
            die_roll.run(
                formula_entry['die_roll']['input'],
                additional_input)
    elif isinstance(formula_entry, dict) \
            and 'conditional' in formula_entry:
        value = \
            conditional.run(
                formula_entry['conditional']['input'],
                additional_input)
    elif not additional_input is None \
            and formula_entry in additional_input:
        value = str(additional_input[formula_entry])
    else:
        exception = True
        value = 'Invalid option: "[' + formula_entry + ']"!'
    return value, exception


def run(run_input, additional_input=None):
    # TODO: update docstring
    """_summary_

    Args:
        run_input (_type_): _description_
        additional_input (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    result = 0
    formula = ''
    exception = False
    if run_input:
        for run_entry in run_input:
            if run_entry == 'formula':
                for formula_entry in run_input['formula']:
                    value, exception = get_formula_entry(
                        run_input[run_entry][formula_entry], additional_input)
                    if not exception:
                        formula = formula + str(value)
                    else:
                        result = value
                    # if isinstance(run_input[run_entry][formula_entry], int):
                    #     formula = formula + \
                    #         str(run_input[run_entry][formula_entry])
                    # elif run_input[run_entry][formula_entry] in OPERATORS:
                    #     formula = str(formula) + \
                    #         run_input[run_entry][formula_entry]
                    # elif isinstance(run_input[run_entry][formula_entry], dict) \
                    #         and 'die_roll' in run_input['formula'][formula_entry]:
                    #     value = \
                    #         die_roll.run(
                    #             run_input[run_entry][formula_entry]['die_roll']['input'],
                    #             additional_input)
                    #     formula = str(formula) + str(value)
                    # elif isinstance(run_input[run_entry][formula_entry], dict) \
                    #         and 'conditional' in run_input['formula'][formula_entry]:
                    #     value = \
                    #         conditional.run(
                    #             run_input[run_entry][formula_entry]['conditional']['input'],
                    #             additional_input)
                    #     formula = str(formula) + str(value)
                    # elif not additional_input is None \
                    #         and run_input[run_entry][formula_entry] in additional_input:
                    #     formula = str(formula) + \
                    #         str(additional_input[run_input[run_entry]
                    #             [formula_entry]])
                    # else:
                    #     exception = True
                    #     result = 'Invalid option: "[' + \
                    #         run_entry + '][' + formula_entry + ']"!'
            else:
                exception = True
                result = 'Invalid option: ' + run_entry + '!'
    else:
        exception = True
        result = 'Invalid submission: "input" was empty!'

    if not exception:
        result = eval_expression.run(formula)

    return result
