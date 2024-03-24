from django.urls import path
from . import views

# #functions views
# urlpatterns = [
#     path("", views.review),
#     path("thank-you", views.thank_you),
#     path("forms/", views.application)
# ]

#class views
urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank-you", views.thank_you),
    path("forms/", views.application)
]

