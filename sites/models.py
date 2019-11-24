from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=13)


class Site(models.Model):
    cover = models.ImageField(upload_to='sites_images')
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='sites')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('site', args=[str(self.id)])
    




