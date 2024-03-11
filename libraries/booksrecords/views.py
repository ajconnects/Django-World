from django.shortcuts import render, get_object_or_404
from .models import BooksDetails


# Create your views here.
def index(request):
    books_details = BooksDetails.objects.all()
    return render(request, "booksrecords/index.html",{
        "books": books_details
    })

def receivers_details(request,id):
    #receiver_info = BooksDetails.objects.get(id=id) #i can still use pk or id(primary key)
    receiver_info = get_object_or_404(BooksDetails, id=id)
    return render(request, "booksrecords/receiverInfo.html",{
        "title": receiver_info.title,
        "fullname": receiver_info.fullname,
        "address": receiver_info.address,
        "phone": receiver_info.phone, 
        "email": receiver_info.email,
        "rating": receiver_info.rating
    })