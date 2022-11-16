# -*- coding: utf-8 -*-
# TODO: update docstring
"""_summary_

Returns:
    _type_: _description_
"""


def run(run_input, additional_input=None):
    # TODO: update docstring
    """_summary_

    Args:
        run_input (_type_): _description_
        additional_input (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    result = ''
    style = run_input['style']
    print(style)

    if not isinstance(run_input['choice'], int):
        choice = run_input['choice']
        if not additional_input is None and choice in additional_input:
            run_input['choice'] = additional_input[choice]
        else:
            run_input['choice'] = choice
    else:
        run_input['choice'] = str(run_input['choice'])

    choice = str(run_input['choice'])
    table = run_input['choices']

    if choice in table:
        result = table[choice]
    else:
        result = 'no result matched'
    return result
