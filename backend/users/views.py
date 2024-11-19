from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Files


def index(request):
    users = User.objects.all()
    return HttpResponse(''.join([str(user) + '<br>' for user in users]))
