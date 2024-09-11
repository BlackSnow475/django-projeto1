from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'João Vitor',
    })


def contato(request):
    return render(request, 'me-apague/temp.html')


def sobre(request):
    return HttpResponse('sobre')