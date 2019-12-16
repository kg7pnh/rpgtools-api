# -*- coding: utf-8 -*-
"""
Defines the ActionRunner views
"""
import importlib
import inspect
import json
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from api.models.action_runner import ActionRunner
from api.serializers.action_runner import Serializer

def print_frame(comments=None):
  callerframerecord = inspect.stack()[1]    # 0 represents this line
                                            # 1 represents line at caller
  frame = callerframerecord[0]
  info = inspect.getframeinfo(frame)
  print(info.filename)                      # __FILE__     -> Test.py
  print(info.function)                      # __FUNCTION__ -> Main
  print(info.lineno)                        # __LINE__     -> 13
  print(comments)

def run_method(method, method_input, additional_input=None):
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

def iterate_input(action_input, additional_input):
    """
    iterate_input
    """
    response = {}
    if 'method' in action_input:
        method = action_input['method']
        method_input = action_input['input']
        response = {
            method: run_method(method, method_input, additional_input)
        }
    else:
        for entry in action_input:
            print(entry)
            if not additional_input:
                additional_input = response
            if 'method' in action_input[entry]:
                method = action_input[entry]['method']
                response[entry] = run_method(method, action_input[entry]['input'], additional_input)
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

        additional_input = None
        if 'additional_input' in action_runner.data:
            additional_input = action_runner.data['additional_input']

        response = iterate_input(action_input, additional_input)

        return Response(json.loads(json.dumps(response)), status=status.HTTP_201_CREATED)
