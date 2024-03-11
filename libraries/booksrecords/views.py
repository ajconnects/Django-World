from django.shortcuts import render, get_object_or_404
from .models import BooksDetails
from django.db.models import Avg


# Create your views here.
def index(request):
    books_details = BooksDetails.objects.all().order_by("title")
    number_books = books_details.count()
    average_rating = books_details.aggregate(Avg("rating"))

    return render(request, "booksrecords/index.html",{
        "books": books_details,
        "total_number_of_books": number_books,
        "average_rating": average_rating
    })

def receivers_details(request,slug):
    #receiver_info = BooksDetails.objects.get(id=id) #i can still use pk or id(primary key)
    receiver_info = get_object_or_404(BooksDetails, slug=slug)
    return render(request, "booksrecords/receiverInfo.html",{
        "title": receiver_info.title,
        "fullname": receiver_info.fullname,
        "address": receiver_info.address,
        "phone": receiver_info.phone, 
        "email": receiver_info.email,
        "rating": receiver_info.rating
    })