from django.shortcuts import render
from . models import Contact
# Create your views here.
def home(request):
    return render(request, 'home.html')


def chatbot(request):
    return render(request, 'chatbot.html')

def instagram(request):
    return render(request, 'instagram.html')

def snake(request):
    return render(request, 'snake.html')

def todo_list(request):
    return render(request, 'todo.html')

def number(request):
    return render(request, 'number.html')

def whatsapp(request):
    return render(request, 'whatsapp.html')

def turtle(request):
    return render(request, 'turtle.html')

def game(request):
    return render(request, 'game.html')

def restaurant(request):
    return render(request, 'restaurant.html')

def contact(request):
    #contact form database
    if request.method == "POST":
        name == request.POST['name']
        email == request.POST['email']
        subject == request.POST['subject']
        message == request.POST['message']
        contact = models.Home(name=name, email=email, subject=subject, message=message)
        contact.save()
    return render(request, 'home.html')