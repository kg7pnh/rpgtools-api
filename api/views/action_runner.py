# -*- coding: utf-8 -*-
"""
Defines the ActionRunner views
"""
import json
from api.models.action_runner import ActionRunner
from api.models.action_runner import Serializer
from api.views.die_roll import perform_die_roll
from rest_framework import exceptions
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from random import randint

class ActionRunnerRequest(CreateAPIView):
    """
    ActionRunnerRequest
    """
    queryset = ActionRunner.action_runners.all()
    serializer_class = Serializer

    def post(self, request, *args, **kwargs):
        """
        post
        """
        action_runner = Serializer(data=request.data, )
        action_runner.is_valid(raise_exception=True)
        action_input = action_runner.data['action_input']
        
        response_json  = '{'

        for action in action_input:
            method = action_input[action]["Method"]

            if method == 'die-roll':
                per_modifier_type = None
                per_modifier_value = None
                roll_modifier_type = None
                roll_modifier_value = None
                post_modifier_type = None
                post_modifier_value = None
                reroll_condition = None
                reroll_value = None

                die_size = action_input[action]['Input']['die_size']
                die_count = action_input[action]['Input']['die_count']
                if 'per_modifier_type' in action_input[action]['Input']:
                    per_modifier_type = action_input[action]['Input']['per_modifier_value']
                if 'per_modifier_value' in action_input[action]['Input']:
                    per_modifier_value = action_input[action]['Input']['roll_modifier_value']
                if 'roll_modifier_type' in action_input[action]['Input']:
                    roll_modifier_type = action_input[action]['Input']['roll_modifier_type']
                if 'roll_modifier_value' in action_input[action]['Input']:
                    roll_modifier_value = action_input[action]['Input']['roll_modifier_value']
                if 'post_modifier_type' in action_input[action]['Input']:
                    post_modifier_type = action_input[action]['Input']['post_modifier_type']
                if 'post_modifier_value' in action_input[action]['Input']:
                    post_modifier_value = action_input[action]['Input']['post_modifier_value']
                if 'reroll_condition' in action_input[action]['Input']:
                    reroll_condition = action_input[action]['Input']['reroll_condition']
                if 'reroll_value' in action_input[action]['Input']:
                    reroll_value = action_input[action]['Input']['reroll_value']
                
                value = perform_die_roll(die_size,
                                 die_count,
                                 per_modifier_type,
                                 per_modifier_value,
                                 roll_modifier_type,
                                 roll_modifier_value,
                                 post_modifier_type,
                                 post_modifier_value,
                                 reroll_condition,
                                 reroll_value)

                response_json  = response_json + '"'+action+'": '+str(value)+','

        response_json = response_json[:-1] + '}'
        print(response_json)

        return Response(json.loads(response_json),status=200)