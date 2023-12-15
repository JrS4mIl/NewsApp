from django.db import models

# Create your models here.
class Blacklist(models.Model):
    ip=models.CharField(max_length=10)

