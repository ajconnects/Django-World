from django.shortcuts import render
from datetime import date

all_posts =[
    {
        "slug":"hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Michael",
        "date":date(2024, 3, 13),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst i was enjoying the view!",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Delectus labore veritatis ut debitis, eligendi odit voluptatem nobis, error quae aperiam, natus doloremque corrupti atque eveniet deleniti hic explicabo ipsam cumque?"
    },
       {
        "slug":"programming is fun",
        "image": "coding.jpg",
        "author": "AjConnect",
        "date":date(2024, 2, 20),
        "title": "Programming Is Great",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst i was enjoying the view!",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Delectus labore veritatis ut debitis, eligendi odit voluptatem nobis, error quae aperiam, natus doloremque corrupti atque eveniet deleniti hic explicabo ipsam cumque?"
    },
       {
        "slug":"into-the-woods",
        "image": "woods.jpg",
        "author": "James",
        "date":date(2022, 1, 13),
        "title": "Natural At its Best",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst i was enjoying the view!",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Delectus labore veritatis ut debitis, eligendi odit voluptatem nobis, error quae aperiam, natus doloremque corrupti atque eveniet deleniti hic explicabo ipsam cumque?"
    }
]

def get_date(post):
    return post['date']

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts":latest_posts
    })

def posts(request):
    return render(request, "blog/all-post.html",{
        "all_posts":all_posts
    })


def post_details(request, slug):
    return render(request, "blog/post-detail.html")