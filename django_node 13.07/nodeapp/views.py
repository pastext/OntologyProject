from django.shortcuts import render

# Create your views here.

def index_page(request):
    context = {
        'header' : 'Hell world',
        'bruh' : 'Подпись'
    }
    return render(request, 'index.html', context)