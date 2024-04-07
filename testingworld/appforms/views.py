from typing import Any
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, DetailView, ListView, FormView
from .models import UserApplication
from .forms import UserApplicationForm

# Create your views here.
# def home(request):
#     if request.method == 'post':
#         pass

#     return render(request, 'appforms/index.html')

class HomeView(CreateView):
    model = UserApplication
    form_class = UserApplicationForm
    template_name = 'appforms/review.html'
    success_url = 'thank-you'

class ThankYouView(TemplateView):
    template_name = 'appforms/thank_you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Expecting a Feedback Soon!"
        return context

#using the template view to fetch data     #step 1
# class ReviewsListView(TemplateView):
#     template_name = 'appforms/review_list.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user_app = UserApplication.objects.all()
#         context['user_apps'] = user_app
#         return context

#using the list view to fetch data than using the template view step 2 in list view you do not need the get_context_data
class ReviewsListView(ListView):
    template_name = 'appforms/review_list.html'
    model = UserApplication
    context_object_name = 'user_apps' #the default name is (object.list) if we dont use the context_object_name.

#using the template view to select specific data     #step 1
# class SingleAppView(TemplateView):
#     template_name = 'appforms/single_app.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user_id = kwargs["id"]
#         selected_user_app = UserApplication.objects.get(pk=user_id)
#         context['user_app'] = selected_user_app
#         return context

#using the detail views to select a specific data than using the Template View  Step 2 the detail view is more flexible
class SingleAppView(DetailView):
    template_name = 'appforms/single_app.html'
    model = UserApplication
    context_object_name = 'user_app'

