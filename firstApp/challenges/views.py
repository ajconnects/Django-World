from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

# def january(request):
#     return HttpResponse("This working well!")   #strings, html

monthly_challenges = {
    'january': 'Write a Python program to find the factorial of a number.',
    'february': 'Create a simple To-Do list application using Python.',
    'march': 'Implement a program that checks if a given word is a palindrome.',
    'april': 'Build a basic web scraper using Python and BeautifulSoup.',
    'may': 'Develop a simple calculator that can perform basic operations.',
    'june': 'Create a program that generates and prints Fibonacci sequence.',
    'july': 'Build a command-line dictionary application using an API.',
    'august': 'Implement a basic chat application using sockets in Python.',
    'september': 'Write a program to convert temperature from Celsius to Fahrenheit.',
    'october': 'Develop a program that counts the number of words in a text file.',
    'november': 'Build a basic Flask web application with a simple CRUD functionality.',
    'december': None
    #'december': 'Create a program that generates a random password of a given length.'
}

def home(request):
    home_response = render_to_string("home.html")
    return HttpResponse(home_response)

def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months, 
        })

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])

    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a> </li>"

    # #"<li><a href="...">January</a></li><a href="...">February</a></li>..."

    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html",{
            "text": challenge_text,
            "month_name": month
            })
        #using the render
        #response_data = render_to_string("challenges/challenge.html")
        #response_data = f"<h1>{challenge_text}<h1>"  #html 
        #return HttpResponse(response_data)
    except:
        #raise Http404()
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
    


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month") #404 response

    redirect_month = months[month -1] #302 is for redirect
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/  the reverse works with the name path in the urls

    return HttpResponseRedirect(redirect_path)
