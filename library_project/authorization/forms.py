from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "fullname"]
        widgets = {
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Введите ваш email"
            }),
            "fullname": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите ваше имя"
            }),
        }
