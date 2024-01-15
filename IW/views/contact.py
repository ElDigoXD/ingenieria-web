from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
from django_htmx.middleware import HtmxDetails

from IW.forms import ContactForm




@require_GET
def contact(request: HttpRequest) -> HttpResponse:
  return render(request, "contact.html")

@require_POST
def contact_form(request: HttpRequest) -> HttpResponse:
  form = ContactForm(request.POST)
  print(form.data, form.is_valid())
  return render(request, "contact-form-response.html")
  