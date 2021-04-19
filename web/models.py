from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=355)
    date = models.DateTimeField('publish date')
    price = models.BigIntegerField('USD')
    user = models.ForeignKey(User, models.CASCADE)
