from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
def starting_page(request):
    #home_response = render_to_string("index.html")
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/all-posts.html")


def post_detail(request):
    pass