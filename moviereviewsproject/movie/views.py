from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse('<h1> welcome to homepage </h1>')
    #return render(request, 'home.html')
    return render(request, 'home.html' , {'name' : 'Camilo Córdoba'})

def aboutPage(request):
    return render(request, 'aboutPage.html')