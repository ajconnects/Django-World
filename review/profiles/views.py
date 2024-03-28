from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

# Create your views here.
def store_file(file):
    with open("temp/image.jpg", "wb+") as img_file:
        for chunk in file.chunks():
            img_file.write(chunk)


class CreateProfileView(View):
    def get(self, request):
        return render(request, "profiles/create_profile.html")
    
    def post(self, request):
        print(request.FILES["image"])
        return HttpResponseRedirect("/profiles")
