from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def review(request):
    if request.method == 'POST':
        entered_username = request.POST['username']
        entered_password = request.POST['password']

        if entered_username == "" or entered_password == "":
            return render(request, "user_review/review.html",{
                "has_error": True
            })
        print(entered_username, entered_password)
        return HttpResponseRedirect("/thank-you")
    
    return render(request, "user_review/review.html", {
        "has_error": False
    })

def thank_you(request):
    return render(request, "user_review/thank_you.html")

def application(request):
    return render(request, "user_review/application.html")