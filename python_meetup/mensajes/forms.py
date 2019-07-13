from django import forms
from python_meetup.mensajes.models import Mensaje

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['titulo','autor','mensaje']