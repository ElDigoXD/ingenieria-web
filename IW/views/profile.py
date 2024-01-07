


from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render, resolve_url, get_list_or_404
from django_htmx.http import HttpResponseClientRedirect
from django.contrib.auth.models import User, Group

from IW.chart import Chart, Dataset, Scale
from IW.settings import DEBUG

def profile(request: HttpRequest) -> HttpResponse:
  if request.POST:
    if request.POST.get("client"):
      return HttpResponseClientRedirect(resolve_url(to=f"profile/{request.POST.get("client")}")) 
    
  context = {
    "weight": "70",
    "chart": Chart(
      canvas_id="a",
      datasets=[Dataset("[68,70,72,70,70,70,68,68,67]")],
      x_labels=str(list(range(1, 15))),
      scales=[Scale()]
      ),
  }
  return render(request, "profile.html", context)


def profile_id(request: HttpRequest, id: int) -> HttpResponse:
  user: User = request.user  # type: ignore

  if not user.is_active or user.groups.get().name != 'Nutricionist' or not DEBUG:
    raise Http404("")
  
  client = User.objects.filter(id=id).first()
  if not client:
    raise Http404("")
    
  
  context = {
    "nutricionist": True,
    "client": client, 
    "weight": "70",
    "chart": Chart(
      canvas_id="a",
      datasets=[Dataset("[68,70,72,70,70,70,68,68,67]")],
      x_labels=str(list(range(1, 15))),
      scales=[Scale()]
      ),
  }
  return render(request, "profile.html", context)
