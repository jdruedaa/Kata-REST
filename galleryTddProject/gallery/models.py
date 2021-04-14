from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000, null=True)
    type = models.CharField(max_length=5, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)


class Portfolio(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
    imagenesPublicas = models.ManyToManyField(Image, related_name='imagenesPublicas')
    imagenesInv = models.ManyToManyField(Image, through='Portfolio_Image', related_name='imagenesInv')


class Portfolio_Image(models.Model):
    imagen = models.ForeignKey(Image, null=True, on_delete=models.PROTECT)
    privacidad = models.IntegerField()
    portfolio = models.ForeignKey(Portfolio, null=True, on_delete=models.PROTECT)
