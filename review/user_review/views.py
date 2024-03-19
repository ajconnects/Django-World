from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def review(request):
    if request.method == 'POST':
        entered_username = request.POST['username']
        print(entered_username)
        return HttpResponseRedirect("/thank-you")
    
    return render(request, "user_review/review.html")

def thank_you(request):
    return render(request, "user_review/thank_you.html")

def application(request):
    return render(request, "user_review/application.html")