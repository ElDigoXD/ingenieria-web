


from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, resolve_url
from django_htmx.http import HttpResponseClientRedirect

from IW.chart import Chart, Dataset, Scale

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
