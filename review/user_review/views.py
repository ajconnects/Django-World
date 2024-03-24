from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import UserReviewForm
from .models import UserReview


# Create your views here.
class ReviewView(View):
    def get(self, request):
        form = UserReviewForm()

        return render(request, "user_review/review.html",{
            'form': form
        })

    def post(self, request):
        form = UserReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you')



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

def thank_you(request):
    return render(request, "user_review/thank_you.html")

def application(request):
    return render(request, "user_review/application.html")