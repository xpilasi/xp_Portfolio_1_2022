from django import forms
from .models import EnviarContacto

class FormularioContacto(forms.ModelForm):
    class Meta:
        model = EnviarContacto
        fields = '__all__'