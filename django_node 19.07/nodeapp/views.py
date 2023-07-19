from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import elements, classes

# Create your views here.

def index_page(request):
    #Elements = elements.objects.all()
    context = {
        'header' : 'Hell world',    
        'bruh' : 'Подпись',
        'elements' : elements.objects.all(),
        'classes' : classes.objects.all(),
    }
    return render(request, 'index.html', context)