from django.db import models


# Create your models here.

class Main(models.Model):
    name = models.CharField(max_length=30)
    about = models.TextField()
    fb = models.CharField(max_length=30, default="")
    tw = models.CharField(max_length=30, default="")
    yt = models.CharField(max_length=30, default="")
    set_name = models.CharField(max_length=30, default="")
    tell = models.CharField(max_length=30, default="")
    link = models.CharField(max_length=30, default="")

    picurl = models.TextField(default="")
    picname = models.TextField(default="")

    picurl2 = models.TextField(default="")
    picname2 = models.TextField(default="")

    def __str__(self):
        return self.set_name
