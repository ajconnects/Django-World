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
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews/", views.ReviewsListView.as_view()),
    path("reviews/favorite", views.AddFavoriteView.as_view()),
    path("reviews/<int:pk>", views.SingleReviewView.as_view()), #on function use id
    path("forms/", views.application)
]

