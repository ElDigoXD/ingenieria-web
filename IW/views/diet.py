from datetime import date, timedelta
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def diet(request: HttpRequest) -> HttpResponse:
  date_min = date(2024, 1, 1)
  date_max = date(2024, 1, 10)
  date_selected = date.today()
  
  
  if request.POST:
    form_date_iso = request.POST.get("date")
    form_next = request.POST.get("next")
    form_prev = request.POST.get("prev")
    if form_date_iso:
      form_date = date.fromisoformat(form_date_iso)
      if form_next:
        date_selected = form_date + timedelta(days=1)
      elif form_prev:
        date_selected = form_date - timedelta(days=1)
      else:
        date_selected = form_date
  else:
    pass
      
  context = {
    "date_min": date_min.isoformat(),
    "date_max": date_max.isoformat(),
    "date_selected": date_selected.isoformat(),
  }
  return render(request, "diet.html", context)