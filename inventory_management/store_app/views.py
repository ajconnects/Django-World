from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, 'store_app/index.html')

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #User: User is a model provided by Django's authentication system. It represents a user account in the database and comes with fields like username, password, email, first name, last name, etc. and use create_user to create and add to the database.
        user_detail = User.objects.create_user(username, email, pass1)
        user_detail.first_name= fname
        user_detail.last_name = lname

        user_detail.save()

        messages.success(request, "Your Account has been successfully created")

        return redirect('signin')

    return render(request, 'store_app/signup.html')

def signin(request):
    return render(request, 'store_app/signin.html')

def signout(request):
    return render(request, 'store_app/signout.html')



