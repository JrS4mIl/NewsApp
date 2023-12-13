from django.db import models

# Create your models here.
from django.db import models


# Create your models here.

class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    txt=models.TextField()
    created_date = models.DateTimeField(blank=True, auto_now_add=True)


    def __str__(self):
        return self.name
