from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', default='default_avatar.jpg')
    bio = models.CharField(max_length=500, null=True, blank=True)
    telephone = models.CharField(max_length=13, blank=True, null=True) 

    def __str__(self):
        return self.username
