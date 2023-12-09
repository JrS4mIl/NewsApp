from django.db import models
from django.utils.text import slugify

# Create your models here.

class News(models.Model):
    name = models.CharField(max_length=150)
    short_txt = models.TextField()
    body_txt = models.TextField()
    date = models.CharField(max_length=12)
    picname = models.TextField()
    picurl=models.TextField(default="0")
    writer = models.CharField(max_length=50)
    slug=models.SlugField(max_length=150,default='')
    catname=models.CharField(max_length=50,default="")
    catid=models.IntegerField(default=0)
    ocatid = models.IntegerField(default=0)
    show=models.IntegerField(default=0)
    update_date = models.DateTimeField(blank=True, auto_now=True)
    created_date = models.DateTimeField(blank=True, auto_now_add=True)



    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)
