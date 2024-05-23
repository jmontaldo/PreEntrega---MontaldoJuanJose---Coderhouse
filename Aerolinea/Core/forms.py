from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class CustomAutenthicationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['Username', 'Password']

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget = forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = { k:"" for k in fields}