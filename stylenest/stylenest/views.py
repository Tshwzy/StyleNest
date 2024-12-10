#from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')

def servicespage(request):
    return render(request, 'Services.html')
    



