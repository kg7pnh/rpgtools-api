# -*- coding: utf-8 -*-
"""
Defines the die_roll actions
"""
import json
from . import addition
from . import average
from . import die_roll

def run(input):
    """
    def
    """

    response_json = '{'

    for stat in input:
        response_json  = response_json + '"'+stat+'": 0,' 
        print(stat)

    
    response_json = response_json[:-1] + '}'

    return json.loads(response_json)
