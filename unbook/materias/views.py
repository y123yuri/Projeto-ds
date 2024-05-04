from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'UnBook.html', {})

def somos(request):
    return render(request, 'Quem_somos.html')