from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting, ChequingAccount

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()


    return render(request, 'db.html', {'greetings': greetings})

def create_chequing(request):

    chequing = ChequingAccount()
    chequing.save()

    accounts = ChequingAccount.objects.all()


    return render(request, 'accounts.html', {'accounts': accounts})

