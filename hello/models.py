from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)


class ChequingAccount(models.Model):
    balance = models.FloatField(default=0)
    name = models.CharField(max_length=60, default="main")

class Goals(models.Model):
    balance = models.FloatField(default=0)
    goal = models.FloatField(default=0)
    name = models.CharField(max_length=60, default="main")
