from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm


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


class Food(models.Model):
  food_type = models.CharField(max_length=50)
  name = models.CharField(max_length=50)
  calories = models.FloatField()
  protein = models.FloatField()
  carbohydrates = models.FloatField()
  fat = models.FloatField()
  g_per_ration = models.FloatField()
  notes = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def __dict__(self):
    return {
        "id": self.id, # type: ignore
        "food_type": self.food_type.capitalize(),
        "name": self.name.capitalize(),
        "calories": self.calories,
        "protein": self.protein,
        "carbohydrates": self.carbohydrates,
        "fat": self.fat,
        "g_per_ration": self.g_per_ration,
        "notes": self.notes.capitalize(),
    }


class FoodForm(ModelForm):
  class Meta:
    model = Food
    fields = ["food_type",
              "name",
              "calories",
              "protein",
              "carbohydrates",
              "fat",
              "g_per_ration",
              "notes"]
