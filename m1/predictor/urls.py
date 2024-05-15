
from django.urls import path
from . import views

urlpatterns = [
    path("", views.predict1, name="predict1"),
    path("dt/", views.predict2, name="predict2" ),
    path("nb/", views.predict3, name="predict3"),
]