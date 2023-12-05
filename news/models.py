from django.db import models


# Create your models here.

class News(models.Model):
    name = models.CharField(max_length=30)
    short_txt = models.TextField()
    body_txt = models.TextField()
    date = models.CharField(max_length=12)
    pic = models.TextField()
    writer = models.CharField(max_length=50)
    slug=models.SlugField(max_length=20,default='')

    def __str__(self):
        return self.name
