from django import forms
from .models import Suscriptor


class SuscriptorForm(forms.ModelForm):
    class Meta:
        model = Suscriptor
        fields = ['correo']
        widgets = {
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'tucorreo@ejemplo.cl',
            }),
        }