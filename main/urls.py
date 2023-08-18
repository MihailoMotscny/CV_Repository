from django.urls import path,include
from main import views
from exchange.views import exchange
from main.views import addimage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('exchange/', exchange,name='exchange'),
    path('addimage/', addimage,name='addimage'),


]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)