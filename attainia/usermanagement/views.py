import json
from attainia.settings import USER_DATA

from rest_framework import viewsets
from rest_framework.response import Response

from .models import UserActivity
from .serializers import UserSerializer


class UserActivityViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed and to filter returned users
    by logins. Gets user data from json file.
    """
    queryset = UserActivity.objects.all().order_by('-last_login')
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


class UserActivityModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed and to filter returned users
    by logins. This one works with the user model and user activity model.
    """
    queryset = UserActivity.objects.all().order_by('-last_login')
    serializer_class = UserSerializer

    def list(self, request):
        queryset = UserActivity.objects.all().order_by('-last_login')
        loggedin = self.request.query_params.get('loggedin', None)

        if loggedin is not None:

            if loggedin == "true":
                queryset = UserActivity.objects.filter(login_count__gt=0)
            elif loggedin == "false":
                queryset = UserActivity.objects.filter(login_count=0)

        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
