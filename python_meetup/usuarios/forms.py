from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre')
    password = forms.CharField(label='Contraseña',widget=forms.PasswordInput)