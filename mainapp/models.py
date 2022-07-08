from email.policy import default
from tabnanny import verbose
from time import timezone
from turtle import title
from django.db import models
from django.forms import CharField
from django.utils import timezone
from django.conf import settings

# Create your models here.

#Creo mi clase de páginas:

class PostPortfolio(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nombre proyecto")
    text = models.TextField(max_length=500, verbose_name="Descripción Proyecto")
    image = models.ImageField(default='null', verbose_name="Foto proyecto",upload_to = 'img_portfolio')
    languajes = models.CharField(max_length=350,verbose_name="Lenguajes ocupados")
    framework = models.CharField(default="null",max_length=200,verbose_name="Framework")
    project_date = models.DateTimeField(verbose_name="Fecha realización proyecto")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    uptaded_at = models.DateTimeField(auto_now_add=True, verbose_name='Actualizado')

    def __str__(self):
        return self.title


class Opcion(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Título página')
    slug = models.CharField(unique=True,max_length=150,verbose_name="URL")
    created_at = models.DateTimeField(default=timezone.now,verbose_name="Fecha creación")
    updated_at = models.DateTimeField(default=timezone.now,verbose_name="Fecha modificación") 

    def __str__(self):
        return self.title


class EnviarContacto(models.Model):
    title = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField(default=34)
    message = models.TextField(default='Write your message here :)')

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=100,verbose_name="Título Artículo")
    description = models.TextField(verbose_name="Contenido Blog")
    image = models.ImageField(default='null', verbose_name="Imagen Blog", upload_to='img_blog')
    created_at = models.DateField(verbose_name="Fecha creación")
    updated_at = models.DateField(auto_now_add=True, verbose_name="Fecha actualización")

    def __str__(self):
        return self.title

