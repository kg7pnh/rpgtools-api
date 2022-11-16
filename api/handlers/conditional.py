# -*- coding: utf-8 -*-
# TODO: update docstring
"""
Defines the conditional handler
"""
from api.handlers import die_roll
from api.handlers import calculation  # pylint: disable=cyclic-import
from api.handlers import table

OPERATORS = ['==',
             '<=',
             '<',
             '>=',
             '>']


def evaluate_comparison(test_value: int, operator: str, eval_value: int):
    # TODO: update docstring
    """_summary_

    Args:
        test_value (int): _description_
        operator (str): _description_
        eval_value (int): _description_

    Returns:
        _type_: _description_
    """
    result = None

    if operator == '==':
        result = test_value == eval_value
    elif operator == '<=':
        result = test_value <= eval_value
    elif operator == '<':
        result = test_value < eval_value
    elif operator == '>=':
        result = test_value >= eval_value
    elif operator == '>':
        result = test_value > eval_value
    elif operator == '!=':
        result = test_value != eval_value
    else:
        result = False
    return result


def run_child(run_input, additional_input):
    # TODO: update docstring
    """_summary_

    Args:
        run_input (dict): The parameters used to run the
        additional_input (dict): _description_

    Returns:
        dict:
    """
    result = None
    if 'calculation' in run_input:
        result = \
            calculation.run(run_input['calculation']['input'],
                            additional_input)
    elif 'die_roll' in run_input:
        result = \
            die_roll.run(run_input['die_roll']['input'],
                         additional_input)
    elif 'conditional' in run_input:
        result = \
            run(run_input['conditional']['input'],
                additional_input)
    elif 'table' in run_input:
        result = \
            table.run(run_input['table']['input'],
                      additional_input)
    else:
        res = list(run_input.keys())[0]
        result = 'Invalid Method Option: "' + str(res) + '"!'
    return result


def get_test_value(test_value, additional_input):
    # TODO: update docstring
    """_summary_

    Args:
        test_value (_type_): _description_
        additional_input (_type_): _description_

    Returns:
        _type_: _description_
    """
    result = None
    if not isinstance(test_value, str):
        result = \
            run_child(
                test_value,
                additional_input)
    else:
        result = additional_input[test_value]
    return result


def get_eval_value(condition, additional_input):
    # TODO: update docstring
    """_summary_

    Args:
        condition (_type_): _description_
        additional_input (_type_): _description_

    Returns:
        _type_: _description_
    """
    eval_value = None
    if not isinstance(condition['eval'], int):
        if not isinstance(condition['eval'], str):
            eval_value = \
                run_child(
                    condition['eval'],
                    additional_input)
        else:
            test_eval = condition['eval']
            eval_value = condition['eval'] = additional_input[test_eval]
    else:
        eval_value = condition['eval']
    return eval_value


def run(run_input, additional_input=None):
    # TODO: update docstring
    """_summary_

    Args:
        run_input (dict): The input from used to perform the conditional operation.
        additional_input (dict, optional): The contents of the additional_input from the calling
                                           operation. Defaults to None.

    Returns:
        dict: The result of the conditional exectuion.
    """
    result = 0
    test_value = 0
    eval_value = 0
    operator = ''

    if not isinstance(run_input['test_value'], int):
        run_input['test_value'] = get_test_value(
            run_input['test_value'], additional_input)

    for condition in run_input['conditions']:
        if run_input['conditions'][condition]['test'] in OPERATORS:
            operator = run_input['conditions'][condition]['test']
            test_value = run_input['test_value']
            eval_value = get_eval_value(
                run_input['conditions'][condition], additional_input)

            if evaluate_comparison(test_value, operator, eval_value):
                if not isinstance(run_input['conditions'][condition]['result'], int):
                    if isinstance(run_input['conditions'][condition]['result'], dict):
                        result = run_child(run_input['conditions'][condition]['result'],
                                           additional_input)
                    elif additional_input and \
                            run_input['conditions'][condition]['result'] in additional_input:
                        result = additional_input[run_input['conditions']
                                                  [condition]['result']]
                    else:
                        result = run_input['conditions'][condition]['result']
                else:
                    result = run_input['conditions'][condition]['result']
        else:
            result = 'Invalid Operator: "' + \
                str(run_input['conditions'][condition]['test']) + '"!'

    return result
