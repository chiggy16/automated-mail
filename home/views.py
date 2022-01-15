from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Receiver
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import requests

# Create your views here.


def emo(temp):
    if(temp <= 10):
        emoji = "\U00002744"
    elif(temp <= 20):
        emoji = "\U0001F976"
    elif(temp <= 27):
        emoji = "\U0001F31E"
    elif(temp <= 32):
        emoji = "\U0001F975"
    else:
        emoji = "\U0001F525"
    return emoji


def temperature(city):
    api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=a02074c7bb0eed3979ba7d9a6d64856b"
    response = requests.get(api)
    response = dict(response.json())
    temp = response["main"]["temp"]
    return temp


def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        city = request.POST.get('city')
        receiver = Receiver(name=name, email=email,
                            city=city, date=datetime.today())
        receiver.save()

        temp = temperature(city)
        emoji = emo(temp)
        subject = f"Hi {name}, interested in our services?"
        mess = f"It is currently {temp}" + \
            u"\N{DEGREE SIGN}" + f"C in {city}. {emoji*4}"
        send_mail(
            subject,
            mess,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        messages.success(request, 'Mail has been sent!')
    return render(request, 'index.html')
