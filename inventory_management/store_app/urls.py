from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("signup", views.signup, name='signup'),
    path("signout", views.signout, name='signout'),
    path("signin", views.signin, name='signin'),
    path("product/<str:name>/", views.ProductPageView.as_view(), name='product-list'),
]
