from django.db import models

# Create your models here.
class Manager(models.Model):
    name = models.CharField(max_length=150)
    utxt=models.TextField()
    email=models.TextField(default='')
    ip=models.TextField(default='')
    city=models.TextField(default='')

    def __str__(self):
        return self.name
