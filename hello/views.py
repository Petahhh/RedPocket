from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting, ChequingAccount

import random

# Create your views here.
def index(request):

    chequing = ChequingAccount.objects.filter(name="chequings")[0]


    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html', {"chequing": chequing})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()


    return render(request, 'db.html', {'greetings': greetings})

def create_chequing(request):

    chequing = ChequingAccount(name="chequings")
    chequing.save()

    accounts = ChequingAccount.objects.all()


    return render(request, 'accounts.html', {'accounts': accounts})

def pay_day(request):

    chequing = ChequingAccount.objects.filter(name="chequings")[0]
    chequing.balance += 1000
    chequing.save()


    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html', {"chequing": chequing})

def shopping(request):

    chequing = ChequingAccount.objects.filter(name="chequings")[0]
    chequing.balance -= random.randrange(20, 999)
    chequing.save()


    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html', {"chequing": chequing})
