from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=False, null=False, primary_key=True)
    objects = CustomUserManager()
    events_list = models.TextField(default="",null=True, blank=True)
    college = models.CharField(max_length=100, default="",null=False, blank=False)
    phone_number = models.CharField(max_length=10, default="",null=False, blank=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email
    
