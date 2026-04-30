''' django import models module '''
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    '''User create model'''
    phone_number = models.CharField(max_length=20, blank=True, null=True)
