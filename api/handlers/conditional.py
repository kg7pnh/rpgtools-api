# -*- coding: utf-8 -*-
"""
Defines the conditional handler
"""
from api.handlers import die_roll
from api.handlers import calculation
from api.handlers import table

OPERATORS = ['==',
             '<=',
             '<',
             '>=',
             '>']

def run_child(run_input, additional_input):
    """
    run_child
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


def run(run_input, additional_input=None):
    """
    run
    """
    test = ''
    result = 0

    if not isinstance(run_input['test_value'], int):
        if not isinstance(run_input['test_value'], str):
            run_input['test_value'] = \
                run_child(
                    run_input['test_value'],
                    additional_input)
        else:
            test_value = run_input['test_value']
            run_input['test_value'] = additional_input[test_value]

    for condition in run_input['conditions']:
        test = str(run_input['test_value'])

        if run_input['conditions'][condition]['test'] in OPERATORS:
            test = test + run_input['conditions'][condition]['test']
            if not isinstance(run_input['conditions'][condition]['eval'], int):
                if not isinstance(run_input['conditions'][condition]['eval'], str):
                    run_input['conditions'][condition]['eval'] = \
                        run_child(
                            run_input['conditions'][condition]['eval'],
                            additional_input)
                else:
                    test_eval = run_input['conditions'][condition]['eval']
                    run_input['conditions'][condition]['eval'] = additional_input[test_eval]
            test = test + str(run_input['conditions'][condition]['eval'])

            if eval(test): # pylint: disable=eval-used
                if not isinstance(run_input['conditions'][condition]['result'], int):
                    if isinstance(run_input['conditions'][condition]['result'], dict):
                        result = run_child(run_input['conditions'][condition]['result'], additional_input)
                    elif run_input['conditions'][condition]['result'] in additional_input:
                        result = additional_input[run_input['conditions'][condition]['result']]
                    else:
                        result = run_child(run_input['conditions'][condition]['result'],
                                           additional_input)
                else:
                    result = run_input['conditions'][condition]['result']
        else:
            result = 'Invalid Operator: "' + str(run_input['conditions'][condition]['test']) + '"!'
    return result
