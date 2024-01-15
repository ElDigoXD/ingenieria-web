import json
from typing import Dict
from django.http import Http404, HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.db.models import F

from IW.models import Food
from django.views.decorators.http import require_POST, require_http_methods, require_GET


def foodTable(request: HttpRequest) -> HttpResponse:
  response = render(request, "food.html")
  # response.headers.setdefault("HX-Refresh", "true")
  return render(request, "food.html")


def addFood(request: HttpRequest) -> HttpResponse:
  with open("programa_dietas.csv", encoding="utf-8") as o:

    for line in o.readlines():
      split = line.split(',')
      print(Food(
          food_type=split[0],
          name=split[1],
          calories=split[2],
          protein=split[3],
          carbohydrates=split[4],
          fat=split[5],
          g_per_ration=split[6],
          notes=split[7],
      ))

  return render(request, "index.html")


@require_http_methods(["GET", "POST"])
def food(request: HttpRequest) -> HttpResponse:
  if request.method == "GET":

    search = request.GET.get("search")
    sort = request.GET.get("sort")
    order = request.GET.get("order")
    offset = request.GET.get("offset")
    limit = request.GET.get("limit")

    query = Food.objects.filter()
    count = query.count()
    if search:
      query = query.filter(name__icontains=search)
    if sort and order:
      query = query.order_by(F(sort).asc() if order == "asc" else F(sort).desc())
    if offset and limit:
      query = query[int(offset):int(offset)+int(limit)]

    if limit:
      foods = {
          "total": query.count() if search else count,
          "totalNotFiltered": count,
          "rows": [f.__dict__() for f in query]}
    else:
      foods = [f.__dict__() for f in query]

    return JsonResponse(foods, safe=False)

  # if request.method == "POST":

  try:
    newFood: Dict[str, str] = json.loads(request.body)

    food = Food.objects.get(id=newFood["id"])
    food.food_type = newFood["food_type"]
    food.name = newFood["name"]
    food.calories = int(newFood["calories"])
    food.protein = int(newFood["protein"])
    food.carbohydrates = int(newFood["carbohydrates"])
    food.fat = int(newFood["fat"])
    food.g_per_ration = int(newFood["g_per_ration"])
    food.notes = newFood["notes"]
    food.save()
    return JsonResponse(food.__dict__())

  except:
    raise Http404()
