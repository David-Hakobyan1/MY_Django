from django.db import models
from django.urls import reverse

# Create your models here.

class Create(models.Model):
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=255)

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = 'Name'
        verbose_name_plural = 'Names'
