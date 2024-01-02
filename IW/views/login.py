from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as session_login
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, resolve_url
from django.template import RequestContext
from django.views.decorators.http import require_POST
from django_htmx.http import HttpResponseClientRedirect

def login(request: HttpRequest) -> HttpResponse:
  return render(request, "login.html")

@require_POST
def login_form(request: HttpRequest) -> HttpResponse:
  
  user: User | None = authenticate(username=request.POST.get("username"), password=request.POST.get("password")) # type: ignore
  print(request.POST)
  
  if not user:
    return render(request, "login-form-response.html")
  
  session_login(request, user)
  
  return HttpResponseClientRedirect(resolve_url(to="home"))