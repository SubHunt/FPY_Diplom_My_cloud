from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Files


def index(request):
    files = Files.objects.all()
    print(files)
    # return HttpResponse(''.join([str(user) + '<br>' for user in users]))
    return render(request, 'files.html', {'files': files})
