from django.shortcuts import render

# Create your views here.
def review(request):
    return render(request, "user_review/review.html")

def application(request):
    return render(request, "user_review/application.html")