from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import User, Files


def index(request):
    files = Files.objects.all()
    # return HttpResponse(''.join([str(user) + '<br>' for user in users]))
    return render(request, 'users/files.html', {'files': files})


def single_file(request, files_id):
    file = get_object_or_404(Files, pk=files_id)
    return render(request, 'users/single_file.html', {'file': file})


# def error_view(request, exception):
#     return render(request, '404.html', status=404)
