from django.shortcuts import render
from shop.models import Student

# Create your views here.
def index(request):
    #students = Student.objects.all()
    student1 = Student.objects.create(
        firstname='Alina', lastname='fox', email='alinafox@gmail'
        )
    student1 = Student.objects.create(
        firstname='Albert', lastname='newman', email='newx@gmail'
        )
    student1 = Student.objects.create(
        firstname='bravo', lastname='james', email='jamest@222gmail'
        )
    #students = Student.objects.filter(firstname='Alina')
    students = Student.objects.filter(firstname__endswith='a')
    #Student.objects.filter(firstname__endswith='a').delete()
    return render(request, 'index.html', {'students': students})
