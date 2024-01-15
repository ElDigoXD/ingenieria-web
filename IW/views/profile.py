


from datetime import date, timedelta
from math import nan
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django.urls import reverse
from django_htmx.http import HttpResponseClientRedirect
from django.contrib.auth.models import User, Group
from django.views.decorators.http import require_POST


from IW.chart import Chart, Dataset, Scale
from IW.models import Tracking
from IW.settings import DEBUG

def profile(request: HttpRequest) -> HttpResponse:
  if request.POST:
    if request.POST.get("client"):
      return HttpResponseClientRedirect(resolve_url(to=f"profile/{request.POST.get("client")}")) 
    
    
  if not request.user.is_active or request.user.groups.get().name != 'Client': # type: ignore
    return HttpResponseRedirect(reverse("home"))
    
  context = {
    "client": request.user,
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

  if not user.is_active or (user.groups.get().name != 'Nutricionist' and DEBUG):
    raise Http404("")
  
  client = User.objects.filter(id=id).first()
  if not client:
    raise Http404("")
  
  tracking = Tracking.objects.filter(user=client, date=date.today()).first()
  
  weight = tracking.weight if tracking else None
  
  labels = []
  data = []
  
  all_tracking = Tracking.objects.filter(user=client).order_by("date").all()
  all_tracking = list(all_tracking)

  if all_tracking.__len__() > 0:
    test =  all_tracking[-1].date - all_tracking[0].date
  
  
    tracking_index = 0
    for i in range(test.days+1):
      d = all_tracking[0].date + timedelta(days=0+i)
      labels.append(d.isoformat())
      if all_tracking[tracking_index].date == d:
        data.append(all_tracking[tracking_index].weight)
        tracking_index += 1
      else:
        data.append(nan)
  
  context = {
    "nutricionist": True,
    "client": client, 
    "weight": weight,
    "chart": Chart(
      canvas_id="a",
      datasets=[Dataset(str(data).replace("nan", "NaN"))],
      x_labels=str(labels),
      scales=[Scale()]
      ),
  }
  return render(request, "profile.html", context)

@require_POST
def updateDailyWeight(request: HttpRequest, id: int) -> HttpResponse:
  user: User = request.user  # type: ignore
  if not user.is_active or not request.POST.get("kg"):
    raise Http404("")
  
  client = User.objects.filter(id=id).first()
  
  tracking, _ = Tracking.objects.get_or_create(user=client, date=date.today(), defaults={"weight": 0})
  tracking.weight = int(request.POST.get("kg")) # type: ignore
  tracking.save()
  
  return HttpResponseClientRedirect(resolve_url(to=f"/profile/{id}"))