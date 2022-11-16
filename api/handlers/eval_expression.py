# -*- coding: utf-8 -*-
# TODO: update docstring
"""_summary_

Returns:
    _type_: _description_
"""
import math

ALLOWED_NAMES = {
    k: v for k, v in math.__dict__.items() if not k.startswith("__")
}
ALLOWED_NAMES['int'] = int


def run(input_string):
    # TODO: update docstring
    """_summary_

    Args:
        input_string (string): A mathematical formula represented as a string.

    Raises:
        NameError: Raises an error if a non-allowed name is passed.

    Returns:
        _type_: _description_
    """
    code = compile(input_string, "<string>", "eval")
    for name in code.co_names:
        if name not in ALLOWED_NAMES:
            raise NameError(f"Use of {name} not allowed")

    return eval(code, {"__builtins__": {}}, ALLOWED_NAMES)  # pylint: disable=eval-used


if __name__ == '__main__':
    print(ALLOWED_NAMES)
    print(run('trunc(12.122532)'))
