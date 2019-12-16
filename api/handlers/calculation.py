# -*- coding: utf-8 -*-
"""
Defines the calculation handler
"""
import math
from api.handlers import conditional
from api.handlers import die_roll

def run(run_input, additional_input=None):
    """
    run
    """
    result = 0
    formula = ''
    print('\tinput:         ' + str(run_input))
    print('\tformula:       ' + formula)
    formula_round = ''
    for run_entry in run_input:
        print('\trun_entry:     ' + run_entry)
        if run_entry == 'formula':
            for formula_entry in run_input['formula']:
                print('\tformula_entry:  ' + formula_entry)
                if run_input[run_entry][formula_entry] in ['+', '-', '*', '/', '**', '%', '(', ')', '[', ']', 'int', 'math.trunc', 'math.ceil']:
                    formula = str(formula) + run_input[run_entry][formula_entry]
                elif isinstance(run_input[run_entry][formula_entry], int):
                    formula = formula + str(run_input[run_entry][formula_entry])
                elif 'die_roll' in run_input['formula'][formula_entry]:
                    value = die_roll.run(run_input[run_entry][formula_entry]['die_roll']['input'], additional_input)
                    formula = str(formula) + str(value)
                elif 'conditional' in run_input['formula'][formula_entry]:
                    value = conditional.run(run_input[run_entry][formula_entry]['conditional']['input'], additional_input)
                    formula = str(formula) + str(value)
                elif run_input[run_entry][formula_entry] in additional_input:
                    formula = str(formula) + str(additional_input[run_input[run_entry][formula_entry]])
                else:
                    print("EOL == " + str(formula_entry))
        elif run_entry == 'round':
            formula_round = run_input[run_entry]
    print('\tformula:      ' + str(formula))
    result = eval(formula)
    
    if formula_round == "down":
        result = math.trunc(result)
    elif formula_round == "up":
        result = math.ceil(result)
    elif formula_round == "drop":
        result = int(result)
    else:
        result = int(result)
    return result
