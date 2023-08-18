from django.urls import path,include
from exchange import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.exchange,name='exchange'),
    path('login/', views.logi,name='login'),
    path('register/', views.register,name='register'),
    path('exit/', authViews.LogoutView.as_view(), name='exit'),
    path('addOffer/', views.addOffer, name='addOffer'),
    path('profile/', views.profile, name='profile'),
    path('not_my_profile/', views.not_my_profile, name='not_my_profile'),

]