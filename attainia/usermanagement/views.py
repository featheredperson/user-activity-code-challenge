from django.shortcuts import render
import datetime
import json
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone
from attainia.settings import USER_DATA
from rest_framework import viewsets

from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response



'''
Create a Django Rest Framework application that has an endpoint that can
produce the content of the users.json file. Your application should be
able to return all users, users that have not logged in, and users that
have logged in.
'''



# TODO: set up viewset class to read file on instantiation - change to viewset


class UserActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed and to filter returned users
    by logins.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def list(self, request):
        # return all users, or filter based on login queryparam
        filtered_users = []
        with open(USER_DATA) as json_file:
            user_data = json.load(json_file)
        loggedin = self.request.query_params.get('loggedin', None)

        if loggedin is not None:
            if loggedin == "true":
                for user in user_data:
                    if user["login_count"] > 0:
                        filtered_users.append(user)
            elif loggedin == "false":
                for user in user_data:
                    if user["login_count"] == 0:
                        filtered_users.append(user)
            else:
                # some other value was passed to loggedin
                filtered_users = user_data
        else:
            filtered_users = user_data

        queryset = filtered_users
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


class UserActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed and to filter returned users
    by logins.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def list(self, request):
        # return all users, or filter based on login queryparam
        filtered_users = []
        with open(USER_DATA) as json_file:
            user_data = json.load(json_file)
        loggedin = self.request.query_params.get('loggedin', None)

        if loggedin is not None:
            if loggedin == "true":
                for user in user_data:
                    if user["login_count"] > 0:
                        filtered_users.append(user)
            elif loggedin == "false":
                for user in user_data:
                    if user["login_count"] == 0:
                        filtered_users.append(user)
            else:
                # some other value was passed to loggedin
                filtered_users = user_data
        else:
            filtered_users = user_data

        queryset = filtered_users
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)