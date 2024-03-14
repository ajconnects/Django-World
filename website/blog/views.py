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
        "content": "Mountains are not merely geographical features; they are dynamic landscapes teeming with life, culture, and ecological significance. As we continue to grapple with the challenges of environmental degradation and climate change, it is more important than ever to recognize the importance of mountains and take proactive steps to protect and preserve these majestic natural wonders for future generations to enjoy."
    },
       {
        "slug":"programming-is-fun",
        "image": "coding.jpg",
        "author": "AjConnect",
        "date":date(2024, 2, 20),
        "title": "Programming Is Great",
        "excerpt": "These instructions, known as code, are written in programming languages such as Python, Java, C++, and JavaScript. Through coding, developers can build software applications, websites, mobile apps, and more, transforming abstract ideas into tangible digital experiences.",
        "content": "Programming is not just a technical skill; it's a gateway to endless possibilities, innovation, and personal growth. Whether you're a novice coder or an experienced developer, the journey of learning and mastering programming is an enriching and fulfilling pursuit. By embracing the power of code, we can shape the future, solve the world's most pressing challenges, and make a meaningful impact on the world around us."
    },
       {
        "slug":"into-the-woods",
        "image": "woods.jpg",
        "author": "James",
        "date":date(2022, 1, 13),
        "title": "Natural At its Best",
        "excerpt": "Natural views hold immense significance for both individuals and communities, offering a myriad of benefits beyond their aesthetic appeal. These vistas serve as reminders of the earth's raw beauty and inherent diversity, evoking feelings of wonder, awe, and humility.",
        "content": "Natural views are not merely scenic backdrops; they are living, breathing expressions of the earth's majesty and resilience. As we strive to build a more sustainable and harmonious relationship with the natural world, let us cherish and protect these priceless landscapes, recognizing them as vital sources of inspiration, solace, and wonder for generations to come. By embracing the serenity of natural views, we can cultivate a deeper appreciation for the beauty and interconnectedness of all life on earth."
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
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html",{
        'post': identified_post
    })