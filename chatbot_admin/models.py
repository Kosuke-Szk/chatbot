from django.db import models

class User(models.Model):
  name = models.CharField(max_length=128)

class Account(models.Model):
  user = models.ForeignKey(User, related_name='users')
  username = models.CharField(max_length=100)
  password = models.CharField(max_length=512)