from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserActivity


class UserActivityCreationForm(UserCreationForm):

    class Meta:
        model = UserActivity
        fields = ('username', 'email', 'last_login', 'login_count', 'project_count')


class UserActivityChangeForm(UserChangeForm):

    class Meta:
        model = UserActivity
        fields = ('username', 'email', 'last_login', 'login_count', 'project_count')