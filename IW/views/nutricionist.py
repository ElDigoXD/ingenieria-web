from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User, Group
from django.shortcuts import render


def nutricionist(request: HttpRequest) -> HttpResponse:
  clients = User.objects.filter(groups__name="Client")
  print(clients)

  context = {
      "clients": clients
  }
  return render(request, "nutricionist.html", context)
