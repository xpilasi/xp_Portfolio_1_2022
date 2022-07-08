from django.apps import AppConfig

from django import forms


class MainappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainapp'
    verbose_name = 'Panel de control'


