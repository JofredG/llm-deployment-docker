# chat/forms.py
from django import forms
from .models import Thread, Message

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


class CustomUserAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "class": "block w-full rounded-md border-0 py-1.5 px-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6",
                "autocomplete": "email",
                "required": True,
            }
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "block w-full rounded-md border-0 py-1.5 px-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6",
                "autocomplete": "current-password",
                "required": True,
            }
        )
    )

    class Meta:
        model = get_user_model()
        fields = ("email", "password")


class ThreadForm(forms.ModelForm):
    name = forms.CharField(required=False)
    model = forms.ChoiceField(
        choices=Thread.MODEL_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "mt-1 block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
            }
        ),
        required=False,
    )
    temperature = forms.FloatField(required=False)
    prompt = forms.CharField(required=False)

    class Meta:
        model = Thread
        fields = ["name", "model", "temperature", "prompt"]


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["content"]
