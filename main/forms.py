from django.forms import ModelForm, TextInput

from main.models import Imagess


class Images(ModelForm):
    class Meta:
        model = Imagess
        fields = ['image','idcheckimg']

        widgets = {
            "idcheckimg": TextInput(attrs={
                'class': 'shos',
                'placeholder': 'ID'})

        }