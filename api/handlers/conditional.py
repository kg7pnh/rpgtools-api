# -*- coding: utf-8 -*-
"""
Defines the conditional handler
"""
from api.handlers import die_roll
from api.handlers import calculation
from api.handlers import table

def run(run_input, additional_input=None):
    """
    run
    """
    test = ''
    result = 0
    print('\trun_input:  ' +str(run_input))
    print('\ttest:       ' + str(test))
    print('\ttest_value: ' + str(run_input['test_value']))
    print('\tresult:     ' + str(result))

    if not isinstance(run_input['test_value'], int):
        if not isinstance(run_input['test_value'], str):
            if 'calculation' in run_input['test_value']:
                test_value = calculation.run(run_input['test_value']['calculation']['input'], additional_input)
                run_input['test_value'] = test_value
            elif 'die_roll' in run_input['test_value']:
                test_value = die_roll.run(run_input['test_value']['die_roll']['input'], additional_input)
                run_input['test_value'] = test_value
            elif 'conditional' in run_input['test_value']:
                test_value = run(run_input['test_value']['conditional']['input'], additional_input)
                run_input['test_value'] = test_value
        else:
            test_value = run_input['test_value']
            run_input['test_value'] = additional_input[test_value]

    print('\ttest:       ' + str(test))
    print('\ttest_value: ' + str(run_input['test_value']))
    print('\tresult:     ' + str(result))

    for condition in run_input['conditions']:
        test = str(run_input['test_value'])

        if run_input['conditions'][condition]['test'] in ['==', '<=', '<', '>=', '>']:
            test = test + run_input['conditions'][condition]['test']

        if not isinstance(run_input['conditions'][condition]['eval'], int):
            if not isinstance(run_input['test_value'], str):
                if 'calculation' in run_input['conditions'][condition]['eval']:
                    test_eval = calculation.run(run_input['conditions'][condition]['eval']['calculation']['input'], additional_input)
                    run_input['conditions'][condition]['eval'] = test_eval
                elif 'die_roll' in run_input['conditions'][condition]['eval']:
                    test_eval = die_roll.run(run_input['conditions'][condition]['eval']['die_roll']['input'], additional_input)
                    run_input['conditions'][condition]['eval'] = test_eval
                elif 'conditional' in run_input['conditions'][condition]['eval']:
                    test_eval = run(run_input['conditions'][condition]['eval']['conditional']['input'], additional_input)
                    run_input['conditions'][condition]['eval'] = test_eval
            else:
                test_eval = run_input['conditions'][condition]['eval']
                run_input['conditions'][condition]['eval'] == additional_input[test_eval]

        test = test + str(run_input['conditions'][condition]['eval'])

        print('\ttest:       ' + str(test))

        if eval(test):
            print('\t' + test + ' = ' + str(eval(test)))
            if not isinstance(run_input['conditions'][condition]['result'], int):
                if 'calculation' in run_input['conditions'][condition]['result']:
                    result = calculation.run(run_input['conditions'][condition]['result']['calculation']['input'], additional_input)
                if 'die_roll' in run_input['conditions'][condition]['result']:
                    result = die_roll.run(run_input['conditions'][condition]['result']['die_roll']['input'], additional_input)
                if 'table' in run_input['conditions'][condition]['result']:
                    result = table.run(run_input['conditions'][condition]['result']['table']['input'], additional_input)
                    print(result)
            else:
                result = run_input['conditions'][condition]['result']
    return result
