from django.contrib import admin

from main.models import Imagess
from .models import ExchangePrice

admin.site.register(ExchangePrice)
admin.site.register(Imagess)



