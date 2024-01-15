from django import forms
from django.forms import Form


class ContactForm(Form):
  name = forms.CharField(max_length=50)
  email = forms.EmailField(max_length=50)
  phone = forms.CharField(max_length=50)
  message = forms.CharField(max_length=500)