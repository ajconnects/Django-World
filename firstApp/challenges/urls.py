from django.urls import path
from . import views


urlpatterns = [
    #path("january", views.january),  #the path two strings, and view
    path("", views.index, name="index"),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")  # every importance
]