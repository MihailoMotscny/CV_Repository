from pickle import GET

from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import datetime

from exchange.forms import LoginForm, ExchangeForm
from exchange.models import ExchangePrice


def exchange (request):
    prices = ExchangePrice.objects.all()

    return render(request,'exchange/exchange.html', {'prices': prices})

def profile (request):
    myid = request.user.id
    myProfile = ExchangePrice.objects.all().filter(idcheck=myid)

    return render(request, 'exchange/profile.html', {'myProfile': myProfile})

def not_my_profile (request):
    allmadel = ExchangePrice.objects.all()
    not_my_company_list=[]
    not_my_id_list=[]


    for el in allmadel:
        not_my_company=el.company
        not_my_id=el.idcheck
        not_my_company_list.append(not_my_company)
        not_my_id_list.append(not_my_id)
    print(not_my_id_list)
    print(not_my_company_list)
    return render(request, 'exchange/not_my_profile.html', {'not_my_company_list': not_my_company_list,'not_my_id_list':not_my_id_list})

def register(response):
    error = ''
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():

            form.save()
            return redirect('home')
        else:
            error="Спробуйте ще раз"

    else:
        form = UserCreationForm()
    data = {
        'form': form,
        'error': error,

    }

    return render(response, 'exchange/register.html', data)

def logi(request):
    error=''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login( request,user)
                    return redirect("home")
                else:
                    error='Обліковий запис не знайдено'
            else:
                error='Неправильний логін або пароль'
    else:
        form = LoginForm()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'exchange/login.html', data)


def addOffer(request):
    error = ''
    dtatime= datetime.datetime.now()
    initial_dict = {
        'idcheck': request.user.id,
        'data':dtatime
    }

    user_id=initial_dict

    if request.method == 'POST':
        form=ExchangeForm(request.POST, initial=initial_dict)
        print("Idcheck=",request.POST.get('idcheck'))
        print("data=",request.POST.get('data'))
        print("company=",request.POST.get('company'))
        print("culture=",request.POST.get('culture'))
        print("typeOfProposition=",request.POST.get('typeOfProposition'))
        print("volume=",request.POST.get('volume'))
        print("price=",request.POST.get('price'))
        print("condition=",request.POST.get('condition'))
        if form.is_valid():

            form.save()

        else:
            error = 'Заповніть всі поля'


    form = ExchangeForm(initial=initial_dict)
    data={
        'form':form,

        'user_id':user_id,
        'error':error,

    }

    return render(request, 'exchange/addingOffer.html',data)