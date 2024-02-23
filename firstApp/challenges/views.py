from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    'december': 'Create a program that generates a random password of a given length.'
}

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(challenge_text)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    redirect_month = months[month -1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/

    return HttpResponseRedirect(redirect_path)
