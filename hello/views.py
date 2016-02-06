from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Greeting, ChequingAccount, Goals
from django.http import JsonResponse
from django.core import serializers
import random

from .forms import *

from django.core import serializers
import json

# Create your views here.
def index(request):

    chequing = ChequingAccount.objects.filter(name="chequings")[0]

    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html', 
        {
            "chequing": chequing,
            "newgoal": NewGoal()
        }
    )


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


def init(request):

    chequing = ChequingAccount.objects.filter(name="chequings")[0]
    goals = Goals.objects.all()

    return JsonResponse({
        "data": {
            "goals": json.dumps(goal_fields_to_json(goals)),
            "chequing": serializers.serialize('json', [ chequing, ]),
        }
    })

@csrf_exempt
def save(request):

    data = json.loads(request.body)

    for goal in data["goals"]:
        get_goal = Goals.objects.filter(name=goal["name"])
        if len(get_goal) == 0:
            new_goal = Goals(name=goal["name"])
            new_goal.save()
        else:
            get_goal.balance = goal["balance"]


    goals = Goals.objects.all()
    print(goals)

    return JsonResponse({
        "success": True
    })

@csrf_exempt
def deleteGoal(request):

    name = json.loads(request.body)["name"]

    Goals.objects.filter(name=name).delete()
    return JsonResponse({
        "success": True
    })

def goal_fields_to_json(goals):
    return [
        {
            "balance": goal.balance,
            "goal": goal.goal,
            "name": goal.name,
        } for goal in goals
    ]
