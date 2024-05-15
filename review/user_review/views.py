from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView


from .forms import UserReviewForm
from .models import UserReview


# Create your views here.
# class ReviewView(View):  #using form view
#class ReviewView(FormView): #the createview is create and view
class ReviewView(CreateView):
    #form_class = UserReviewForm  #you dont need a form class with by using the model
    model = UserReview
    form_class = UserReviewForm
    template_name = 'user_review/review.html'  #use for get
    success_url = '/thank-you'   #use for the post with the def form_valid function and by using the urls path on the success_url.

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

    # def get(self, request):
    #     form = UserReviewForm()

    #     return render(request, "user_review/review.html",{
    #         'form': form
    #     })

    # def post(self, request):
    #     form = UserReviewForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('/thank-you')



# #the functions
# def review(request):
#     if request.method == 'POST':
#         #existing_data = UserReview.objects.get(pk=1)
#         form = UserReviewForm(request.POST) #instance=existing_data

#         if form.is_valid():   #is_valid(methods from the form class) to check the validation.
#             # user_review = UserReview(
#             #     user_name=form.cleaned_data['user_name'],
#             #     review_text = form.cleaned_data['review_text'],
#             #     rating = form.cleaned_data['rating'],
#             # )
#             # user_review.save()
#             form.save()
#             #print(form.cleaned_data) #cleaned_data(methods from form) that clean data and it return  a dict to the terminate
#         # entered_username = request.POST['username']
#         # entered_password = request.POST['password']

#         # if entered_username == "" or entered_password == "":
#         #     return render(request, "user_review/review.html",{
#         #         "has_error": True
#         #     })
#         #print(entered_username, entered_password)
#             return HttpResponseRedirect("/thank-you")
#     else:    #you create new form and it use the GET request
#         form = UserReviewForm()

#     return render(request, "user_review/review.html", {
#         "form": form
#     })

class ThankYouView(TemplateView):
    template_name = 'user_review/thank_you.html'
    # def get(self, request):
    #     return render(request, "user_review/thank_you.html")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'This works!'
        return context

# #function
# def thank_you(request):
#     return render(request, "user_review/thank_you.html")

class ReviewsListView(ListView):
    template_name = 'user_review/review_list.html'
    model = UserReview
    context_object_name = "reviews"

    # #doing a filter on the views
    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data

# #or
# class ReviewsListView(TemplateView):
#     template_name = 'user_review/review_list.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = UserReview.objects.all()
#         context['reviews'] = reviews
#         return context

class SingleReviewView(DetailView):
    template_name = 'user_review/single_review.html'
    model = UserReview

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session["favorite_review"]
        context["is_favorite"] = favorite_id == loaded_review.id
        return context

    # #Using the models them on the url set the pk or this function
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs["id"]
    #     selected_reviews = UserReview.objects.get(pk=review_id)
    #     context['review'] = selected_reviews
    #     return context

class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST['review_id']
        #fav_review = UserReview.objects.get(pk=review_id)
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)

def application(request):
    return render(request, "user_review/application.html")