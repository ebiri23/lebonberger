from django.db import models
from datetime import datetime

# Create your models here.
class Conversation(models.Model):
    name = models.CharField(max_length=2000)
class Utalk(models.Model):
    value = models.CharField(max_length=2000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=2000000)
    conversation = models.CharField(max_length=2000000)

class Letter(models.Model):
    name = models.CharField(max_length=2000)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=2000)
    message = models.CharField(max_length=2000000)

class Lettera(models.Model):
    name = models.CharField(max_length=2000)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=2000)
    message = models.CharField(max_length=2000000)