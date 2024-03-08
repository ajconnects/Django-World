from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import Http404
from django.db.models import Avg, Sum

# Create your views here.
def index(request):
    books = Book.objects.all().order_by("title")
    num_books = books.count()
    avg_rating = books.aaggregate(Avg('rating'))

    return render(request, "storagedetails/index.html",{
                    "books": books,
                    "total_number_of_books": num_books,
                    "average_rating": avg_rating
                  })

def book_details(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()  or 
    book = get_object_or_404(Book, slug=slug)
    return render(request, "storagedetails/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling 
    })