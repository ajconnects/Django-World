from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    path("thank-you/", views.ThankYouView.as_view(), name='thank-you'),
    path("reviews", views.ReviewsListView.as_view(), name='reviews-list'),
    path("reviews/<int:pk>", views.SingleAppView.as_view(), name="single-app")
]