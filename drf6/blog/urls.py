from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.PostListCreateView.as_view()),
    path("posts/<int:pk>", views.Post_R_U_D_View.as_view()),
    path("tags/", views.TagListCreateView.as_view()),
    path("tags/<int:pk>", views.Tag_R_U_D_View.as_view()),
]