from django.http import HttpResponse
from django.shortcuts import render
from .forms import EmailForm,ContactForm
from .models import Cars ,Tag

# Create your views here.

def index(request):
    cars = Cars.objects.all()
    tag = Tag.objects.all()
    carousel = cars.filter(tag=Tag.objects.get(name="carousel"))
    feature = cars.filter(tag=Tag.objects.get(name="feature"))
    latest = cars.filter(tag=Tag.objects.get(name="latest"))

    if request.method == 'POST':
        emailForm = EmailForm(request.POST)
        if emailForm.is_valid():
            emailForm.save()
            return HttpResponse("sorov qabul qilindi")
    else:
        emailForm = EmailForm()
    context = {
        'emailForm': emailForm,
        "cars": cars,
        "carousel": carousel,
        "feature": feature,
        "latest": latest,
    }
    return  render(request, 'index.html', context=context)

def contact(request):
    cars = Cars.objects.all()
    carousel = cars.filter(tag=Tag.objects.get(name="carousel"))
    if request.method == "POST":
        contactForm = ContactForm(request.POST)
        if contactForm.is_valid():
            contactForm.save()
            return HttpResponse("<h1>sorov qabul qilindi<h1>")
        else:
            return HttpResponse("<h1>malumotni tog'ri kirit<h1>")
    else:
        contactForm = ContactForm()
    contex = {
        "contactForm": contactForm,
        "carousel": carousel,
    }

    return  render(request, 'contact.html', context=contex)

def detail(request, id ):
    car = Cars.objects.get(id=id)
    context = {
        "x": car
    }
    return render(request,'carsDetail.html', context=context)










