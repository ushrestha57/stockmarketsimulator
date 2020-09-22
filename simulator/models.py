from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Stock(models.Model):
    price = models.TextField()
    quantity = models.TextField()
    name = models.TextField()
    symbol = models.TextField()

class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    netWorth = models.TextField()
    avaliableMoney = models.IntegerField()

class Shares(models.Model):
    amount = models.TextField()
    price = models.TextField()
    name = models.TextField()
    symbol = models.TextField()
    owner = models.ForeignKey(Portfolio, on_delete= models.CASCADE)


