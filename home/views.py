from django.shortcuts import render, HttpResponse, redirect
from .models import Special, FoodItem, Booktable, Newsletter, Contact
from django.contrib import messages

# Create your views here.

def index(request):
    items = FoodItem.objects.all()
    context = {
        'items':items,
    }
    return render(request, 'home/index.html', context)

def newsletter(request):
    if request.method == 'POST':
        email = request.POST['email']
        ref = Newsletter(email = email)
        ref.save()
    messages.success(request, "You have been successfully added to the list.")
    return redirect('/')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        ref = Contact(name = name, email =email, message = message, subject= subject)
        ref.save()
    messages.success(request, 'Your message has been successfully recieved.')
    return redirect('/')

def booktable(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['name']
        phone = request.POST['name']
        date = request.POST['date']
        time = request.POST['time']
        count = request.POST['people']
        message = request.POST['message']
        ref = Booktable(name= name, email= email, phone = phone, date = date, time=time, count = count, message = message)
        ref.save()
    messages.success(request, 'Your table has been successfully queued. Once confirmed you will get confirmation on your email.')
    return redirect('/')
