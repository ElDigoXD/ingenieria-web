from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

def index(request: HttpRequest) -> HttpResponse:
  user: User = request.user; # type: ignore
  group = user.groups.first()
  if not group:
    return render(request, "index.html")
  elif group.name == "Client":
    return redirect("profile")
  elif  group.name == "Nutricionist":
    return redirect("nutricionist")
    
  return render(request, "index.html")
