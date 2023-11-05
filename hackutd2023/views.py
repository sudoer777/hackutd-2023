# views.py

from django.shortcuts import render


def index(request):
    context = {'name': 'World'}
    return render(request, 'index.html', context)

def result(request):
    context = {'name': 'World'}
    return render(request, 'result.html', context)
