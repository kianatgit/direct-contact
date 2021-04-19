from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=355)
    date = models.DateTimeField('publish date')
    price = models.BigIntegerField('USD')
    user = models.ForeignKey(User, models.CASCADE)
    def __str__(self):
        return "%s - %i USD -%s" %(self.title, self.price, self.date)

class Purchaseinq(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=355)
    date = models.DateTimeField('publish date')
    priceTarget = models.BigIntegerField('USD')
    user = models.ForeignKey(User, models.CASCADE)
    def __str__(self):
        return "%s - %i Target Price (USD) - %s" %(self.title, self.priceTarget, self.date)