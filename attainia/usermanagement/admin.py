from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserActivityCreationForm, UserActivityChangeForm
from .models import UserActivity


class UserActivityAdmin(UserAdmin):
    add_form = UserActivityCreationForm
    form = UserActivityChangeForm
    model = UserActivity
    list_display = ['email', 'username', 'last_login', 'login_count', 'project_count']


admin.site.register(UserActivity, UserAdmin)
