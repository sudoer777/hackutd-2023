# views.py

from django.shortcuts import render


def index(request):
    context = {'name': 'World'}
    return render(request, 'my_template.html', context)

def result(request):
    context = {'name': 'World'}
    return render(request, 'my_template.html', context)
