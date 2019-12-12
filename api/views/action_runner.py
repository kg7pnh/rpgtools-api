# -*- coding: utf-8 -*-
"""
Defines the ActionRunner views
"""
import importlib
import json
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from api.models.action_runner import ActionRunner
from api.serializers.action_runner import Serializer

def iterate_input(action_input, additional_input):
    """
    iterate_input
    """
    response = {}
    for entry in action_input:
        if not additional_input:
            additional_input = response
        if 'Method' in action_input[entry]:
            method = action_input[entry]['Method']
            try:
                module_name = 'api.handlers.'+method
                module = importlib.import_module(module_name)
                response[entry] = module.run(action_input[entry]['Input'], additional_input)
            except ImportError as import_error:
                response[entry] = \
                    'Failed to find an action method named '+method+\
                    '('+import_error+').'
        else:
            additional_input = response
            response[entry] = iterate_input(action_input[entry], additional_input)
    return response

class ActionRunnerRequest(CreateAPIView):
    """
    ActionRunnerRequest
    """
    queryset = ActionRunner.objects.all() # pylint: disable=no-member
    serializer_class = Serializer

    def post(self, request, *args, **kwargs):
        """
        post
        """
        action_runner = Serializer(data=request.data, )
        action_runner.is_valid(raise_exception=True)
        action_input = action_runner.data['action_input']

        response = iterate_input(action_input, None)

        # previous_response = None
        # response  = {}

        # for action in action_input:
        #     value = None
        #     method = action_input[action]["Method"]

        #     try:
        #         module_name = 'api.handlers.'+method
        #         module = importlib.import_module(module_name)

        #         json_input = str(action_input[action]['Input']).replace('\'', '"')
        #         action_response = module.run(json.loads(json_input))

        #     except ImportError as error:
        #         action_response = '"Failed to find an action method named '+method+'."'

        #     response[action] = action_response
        return Response(json.loads(json.dumps(response)), status=status.HTTP_201_CREATED)
