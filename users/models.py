from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):

    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)