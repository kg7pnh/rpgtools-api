# -*- coding: utf-8 -*-
# TODO: update docstring
"""Defines the ActionRunner views
"""
import importlib
import json
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from api.models.action_runner import ActionRunner
from api.serializers.action_runner import Serializer


def run_method(method, method_input, additional_input=None):
    # TODO: update docstring
    """run_method
    """
    response = {}
    try:
        module_name = 'api.handlers.'+method
        module = importlib.import_module(module_name)
        response = module.run(method_input, additional_input)
    except ModuleNotFoundError as module_not_found_error:
        response = {
            "error": {
                "message": "Failed to find a method named '" + method + "'}'",
                "exception": str(module_not_found_error)
            }
        }
    return response


def iterate_input(action_input, additional_input, index):
    # TODO: update docstring
    """iterate_input
    """
    response = {}
    if 'method' in action_input and \
            'name' in action_input and \
            'input' in action_input:
        name = action_input['name']
        method = action_input['method']
        method_input = action_input['input']
        response = {
            name: run_method(method, method_input, additional_input)
        }
    else:
        response['error_entry_index_' + str(index)] = \
            'Action Input entries require "name", "method" and "input" items to be processed.'
    return response


class ActionRunnerRequest(CreateAPIView):
    # TODO: update docstring
    """ActionRunnerRequest
    """
    queryset = ActionRunner.objects.all()  # pylint: disable=no-member
    serializer_class = Serializer

    def post(self, request, *args, **kwargs):  # pylint: disable=unused-argument
        # TODO: update docstring
        """post
        """

        result = {}
        action_runner = Serializer(data=request.data, )
        if 'action_input' in action_runner.initial_data:
            action_input = json.loads(json.dumps(
                action_runner.initial_data['action_input']))
            if 'additional_input' in action_runner.initial_data:
                additional_input = json.loads(json.dumps(
                    action_runner.initial_data['additional_input']))
            else:
                additional_input = None
            length = len(action_input)
            for index in range(length):
                response = iterate_input(
                    action_input[index], additional_input, index)
                result.update(response)
                if additional_input:
                    additional_input.update(response)
                else:
                    additional_input = response
        else:
            result['Invalid submission'] = '"action_input" was empty or missing!'

        return Response(json.loads(json.dumps(result)), status=status.HTTP_201_CREATED)
