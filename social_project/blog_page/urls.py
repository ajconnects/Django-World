from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("users/", views.UserListView.as_view(), name="users-list"),
    path("users/<str:username>/", views.UserDetailView.as_view(), name="user-detail"),
    path("posts/", views.PostListView.as_view(), name="posts-list"),
    path("posts/<int:post_id>/", views.PostDetailView.as_view(), name="post-detail"),
    path("users/<str:username>/posts/", views.UserPostView.as_view(), name="user-post"),
    path("register/", views.RegisterUserView.as_view(), name="register"),
    path(
        "users/post/<str:username>/", views.PostCreateView.as_view(), name="create-post"
    ),
    path("users/<str:username>/update/", views.UpdateUserView.as_view(), name='update-user'),
    path("users/<str:username>/delete/", views.DeleteUserView.as_view(), name="delete-user"),
    #path("posts/<int:post_id>/update/", views.UpdatePostView.as_view(), name='update-post'),
    path('users/<str:username>/posts/<int:post_id>/update/', views.UpdatePostView.as_view(), name='update-post'),
    path('users/<str:username>/posts/<int:post_id>/delete/', views.DeletePostView.as_view(), name='delete-post'),
]
