from django.db import models

# Create your models here.

class Bank(models.Model):
    accountnumber=models.IntegerField()
    username=models.CharField( max_length=50)
    balance=models.IntegerField()
    withdraw=models.IntegerField()
    deposit=models.IntegerField()
