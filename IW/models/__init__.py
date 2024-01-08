from django.contrib.auth.models import User
from django.db import models

class UserData(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  weight = models.IntegerField()
  height = models.IntegerField()
  activity = models.FloatField()
  phone = models.CharField(max_length=20)
  
class Tracking(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  date = models.DateField()
  weight = models.IntegerField()