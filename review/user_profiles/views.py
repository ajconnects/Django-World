from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView

from .forms import ProfileFrom
from .models import UserProfile

# Create your views here.
#store the file from the user
# def store_file(file):
#     with open("temp/image.jpg", "wb+") as dest:
#         for chunk in file.chunks():  #the chunks is from django(uploadedfile.read)
#             dest.write(chunk)

#for the view

class CreateProfileView(CreateView):
    template_name = "user_profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"


class ProfilesView(ListView):
    model = UserProfile
    template_name = "user_profiles/user_profiles.html"
    context_object_name = "profiles"



# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileFrom()
#         return render(request, "user_profiles/create_profile.html", { "form": form })

#     def post(self, request):
#         submitted_form = ProfileFrom(request.POST, request.FILES)

#         # valid the forms
#         if submitted_form.is_valid():
#         #we call store_file function so the file can be save in tmp folder
#             #store_file(request.FILES["image"]) #you get access to file by using the FILES method in the request in html you give it same name input name.
#             profile = UserProfile(image=request.FILES["user_image"])
#             profile.save()
#             return HttpResponseRedirect("/profiles")

#         return render(request, "user_profiles/create_profile.html", { "form": submitted_form})
