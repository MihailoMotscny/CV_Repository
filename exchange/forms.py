from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput

from exchange.models import ExchangePrice


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ExchangeForm(ModelForm):
    class Meta:
        model = ExchangePrice
        fields = ['company','culture','price','data','idcheck','typeOfProposition','condition','volume']

        widgets = {
            "company":TextInput(attrs={
                'class':'form-control',
                'placeholder':'Назва компанії'
            }),

            "culture": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Культура'
            }),

            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ціна'
            }),

            "data": DateTimeInput(attrs={
                'class': 'shos',
                'placeholder': 'Дата'
            }),

            "idcheck": TextInput(attrs={
                'class': 'shos',
                'placeholder': 'ID'

            }),

            "typeOfProposition": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тип пропозиції'
            }),

            "condition": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Умови'
            }),

            "volume": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Об'єм"
            })

        }