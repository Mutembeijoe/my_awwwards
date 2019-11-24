from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=13)

    def __str__(self):
        return self.name


class Site(models.Model):
    cover = models.ImageField(upload_to='sites_images')
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='sites')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('site', args=[str(self.id)])
    
class Rating(models.Model):
    design = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )

    usability = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )

    content = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )

    site = models.ForeignKey(Site, related_name='rating', on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), related_name='ratings', blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return f'D:{self.design}, U:{self.usability}, C:{self.content} '




