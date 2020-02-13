'''
Creating a regular serializer for working with json from the datafile, and
a model serializer for working with it from the database
'''
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.EmailField()
    # django's user model's max length is 150
    username = serializers.CharField(max_length=150)
    last_login = serializers.DateTimeField()
    login_count = serializers.IntegerField(min_value=0)
    project_count = serializers.IntegerField(min_value=0)


