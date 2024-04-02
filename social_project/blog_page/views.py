from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import User, Post
from .form import UserForm, PostForm
from django.urls import reverse_lazy
import logging
import datetime


logger = logging.getLogger(__name__)


# Create your views here.
#home page
class HomePageView(TemplateView):
    template_name = "blog_page/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logging.warning(f'someone visited the home page at {datetime.datetime.now()}')
        return context

#user list
class UserListView(ListView):
    model = User
    context_object_name = "users"
    template_name = "blog_page/user_list.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context= super().get_context_data(**kwargs)
        logger.info('someone want our users list')
        return context

#user profile
class UserDetailView(DetailView):
    model = User
    context_object_name = "user"
    template_name = "blog_page/user_profile.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    # pk_url_kwarg = 'id'

#view all post
class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog_page/post_list.html"


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog_page/post_detail.html"
    pk_url_kwarg = "post_id"


class UserPostView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog_page/user_post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
        username = self.kwargs["username"]
        user = get_object_or_404(User, username=username)
        context["user"] = user
        # print(context)
        return context

    def get_queryset(self):
        username = self.kwargs["username"]
        user = get_object_or_404(User, username=username)
        return Post.objects.filter(user=user).order_by("-created_at")  # here is display


class RegisterUserView(CreateView):
    model = User
    form_class = UserForm
    template_name = "blog_page/register.html"
    success_url = reverse_lazy("users-list")

    def form_valid(self, form):
        response = super().form_valid(form)
        logging.warning(f"{self.object.username} is created")
        return response


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog_page/post_create.html"
    slug_url_kwarg = 'username'
    slug_field = 'username'

    def form_valid(self, form):
        user = get_object_or_404(User, username=self.kwargs["username"])
        form.instance.user = user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "user-detail", kwargs={"username":self.object.user.username}
        )  #


class UpdateUserView(UpdateView):
    model = User
    form_class = UserForm
    template_name = "blog_page/register.html"
    
    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])
    
    def get_success_url(self) -> str:
        return reverse_lazy('user-detail', kwargs={'username':self.object.username})
    
    def form_valid(self, form):
        response = super().form_valid(form)
        logger.debug(self.request)
        logger.info(f"User updated: {self.object.username}")
        return response
    
class DeleteUserView(DeleteView):
    model = User
    template_name = "blog_page/delete_user.html"
    success_url = reverse_lazy('users-list')
    slug_url_kwarg = 'username'
    slug_field = 'username'

#my solution
# class UpdatePostView(UpdateView):
#     model = Post
#     form_class = PostForm
#     template_name = "blog_page/post_create.html"
#     success_url = reverse_lazy('posts-list')
#     pk_url_kwarg = 'post_id'


class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog_page/post_create.html"
    slug_url_kwarg = 'username'
    slug_field = 'username'
    pk_url_kwarg = 'post_id'

    def get_object(self):
        return get_object_or_404(Post, id=self.kwargs['post_id'])
    
    def get_success_url(self):
        return reverse_lazy('user-post', kwargs={'username':self.object.user.username})

    
class DeletePostView(DeleteView):
    model = Post
    template_name = "blog_page/delete_post.html"
    slug_url_kwarg = 'username'
    slug_field = 'username'
    pk_url_kwarg = 'post_id'
    
    def get_success_url(self):
        return reverse_lazy('user-post', kwargs={'username':self.object.user.username})
