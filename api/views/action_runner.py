# -*- coding: utf-8 -*-
"""
Defines the ActionRunner views
"""
import json
from api.models.action_runner import ActionRunner
from api.models.action_runner import Serializer
# from api.actions.die_roll import run
from rest_framework import exceptions
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from random import randint

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
        
        previous_response = None
        response_json  = '{'

        for action in action_input:
            value = None
            method = action_input[action]["Method"]

            try:
                module = 'api.actions.'+method
                __import__ (module)
                json_input = str(action_input[action]['Input']).replace('\'', '"')
                value = run(json.loads(json_input))
            except ImportError as error:
                value = '"Failed to find a module named '+method+'.'

            response_json  = response_json + '"'+action+'": '+str(value)+','

        response_json = response_json[:-1] + '}'

        return Response(json.loads(response_json),status=status.HTTP_201_CREATED)
