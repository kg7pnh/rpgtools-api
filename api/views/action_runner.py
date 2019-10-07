# -*- coding: utf-8 -*-
"""
Defines the ActionRunner views
"""
import importlib
import json
from api.models.action_runner import ActionRunner
from api.models.action_runner import Serializer
# from api.actions.die_roll import run
from rest_framework import exceptions
from rest_framework import serializers
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from random import randint

def iterate_input(input, additional_input):
    """
    iterate_input
    """
    response = {}
    for entry in input:
        print(entry)
        if not additional_input:
            additional_input = response
        if 'Method' in input[entry]:
            method = input[entry]['Method']
            try:
                module_name = 'api.actions.'+method
                module = importlib.import_module(module_name)
                response[entry] = module.run(input[entry]['Input'], additional_input)
            except ImportError as error:
                response[entry] = '"Failed to find an action method named '+method+'."'
        else:
            additional_input = response
            response[entry] = iterate_input(input[entry], additional_input)
    return response

class ActionRunnerRequest(CreateAPIView):
    """
    ActionRunnerRequest
    """
    queryset = ActionRunner.objects.all()
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
        #         module_name = 'api.actions.'+method
        #         module = importlib.import_module(module_name)

        #         json_input = str(action_input[action]['Input']).replace('\'', '"')
        #         action_response = module.run(json.loads(json_input))

        #     except ImportError as error:
        #         action_response = '"Failed to find an action method named '+method+'."'

        #     response[action] = action_response
        return Response(json.loads(json.dumps(response)),status=status.HTTP_201_CREATED)
