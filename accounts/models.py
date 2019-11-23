from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', default='default_avatar.jpg')
    bio = models.CharField(max_length=500)
    telephone = models.CharField(max_length=13)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.username
        