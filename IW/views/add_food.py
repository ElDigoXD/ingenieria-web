import sys
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from IW.models import Food


def addFood(request: HttpRequest) -> HttpResponse:

  with open("programa_dietas.csv", encoding="utf-8") as o:
    
    for line in o.readlines():
      split = line.split(',')
      print (Food(
          food_type=split[0],
          name=split[1],
          calories=split[2],
          protein=split[3],
          carbohydrates=split[4],
          fat=split[5],
          g_per_ration=split[6],
          notes=split[7],
      ))
    pass

  return render(request, "index.html")
