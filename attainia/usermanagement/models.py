from django.db import models
from django.contrib.auth.models import AbstractUser


class UserActivity(AbstractUser):
    class Meta:
        ordering = ['-last_login']
        verbose_name_plural = "users"
        # app_label = 'usermanagement'

    last_login = models.DateTimeField()
    login_count = models.IntegerField()
    project_count = models.IntegerField()

    def __str__(self):
        return self.username + " " + str(self.last_login)
