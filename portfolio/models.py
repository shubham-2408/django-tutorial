from django.db import models
from django.db.models import BigIntegerField
from django.forms import CharField


# Create your models here.
class Job(models.Model):
    company = models.CharField(primary_key=True)
    description = models.CharField()
    image = models.ImageField(upload_to ='image/')
