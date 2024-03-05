from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
def home(request):
    home_response = render_to_string("home.html")
    return HttpResponse(home_response)

