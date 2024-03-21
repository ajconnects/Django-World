from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserReviewForm

# Create your views here.
def review(request):
    if request.method == 'POST':
        form = UserReviewForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
        # entered_username = request.POST['username']
        # entered_password = request.POST['password']

        # if entered_username == "" or entered_password == "":
        #     return render(request, "user_review/review.html",{
        #         "has_error": True
        #     })
        #print(entered_username, entered_password)
            return HttpResponseRedirect("/thank-you")
    else:   
        form = UserReviewForm()

    return render(request, "user_review/review.html", {
        "form": form
    })

def thank_you(request):
    return render(request, "user_review/thank_you.html")

def application(request):
    return render(request, "user_review/application.html")