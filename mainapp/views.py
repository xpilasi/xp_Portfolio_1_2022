from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import get_object_or_404, render
from .forms import FormularioContacto
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request,'index.html',{
        'title': 'Home',
        'title_page': ''
    })

def aboutMe(request):
    string = 'Una string de prueba'
    interior = string[0:7]
    return render(request,'about-me.html', {
        'title': 'About Me',
        'title_page': 'About Me',
        'interior': interior
    })

def portfolio(request):
    return render(request,'portfolio.html', {
        'title': 'Porftolio',
        'title_page': 'Projects'
    })

def blog(request):
    return render(request,'blog.html', {
        'title': 'Blog',
        'title_page': 'Blog'
    })


def contact(request):

   
    #Meto el objeto del formulario en una variable
    
    formulario = FormularioContacto()

    if request.method == "POST":
        
        formulario = FormularioContacto(request.POST) #Con esto el formulario queda lleno
        
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Thanks for your message! I'll contact you within the next 24 hrs :) ")
            return redirect('contact')
       
        
    return render(request,'contact.html', {
        'form' : formulario,
        'title': 'Contact',
        'title_page': 'Contact'

    }) #aquí viaja la info que lleva el formulari0

def nueva(request):
    return render(request,'nueva.html')

def cositas(request):
    return render(request,'cositas.html',{
        'title': '#cositas',
        'title_page': '#cositas'
    })

#Formulario de contacto

def enviarMensaje(request):

    return render(request,'blog.html')

