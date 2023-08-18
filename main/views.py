from django.shortcuts import render, redirect

from exchange.models import ExchangePrice
from main.forms import Images
from main.models import Imagess


def home(request):

    seeds=ExchangePrice.objects.all()
    seedsd=list(seeds.values())
    dicc=[]
    controllist=[]
    x=0
    for element in seedsd:
        if len(dicc) == 0:
            dicc.append(element)
            controllist.append(element['culture'])
        x += 1
        y = 0
        for element1 in dicc:
            y += 1
            if element['culture'] == element1['culture']:
                if int(element['price']) < int(element1['price']):
                    element1['price'] = element['price']
                else:
                    continue
            else:
                if x > 1 and element['culture'] not in controllist:
                    dicc.append(element)
                    break

    myid = request.user.id
    if len(Imagess.objects.all().filter(idcheckimg=myid)) !=0:
        image = Imagess.objects.all().filter(idcheckimg=myid)
        linktoimage = ''
        for el in image:
            linktoimage = el.image
        return render(request, 'main/home.html', {'linkto': linktoimage,'dicc': dicc})
    else:
        return render(request, 'main/home.html', {'dicc': dicc})


def about (request):
    return render(request,'main/about.html')


def addimage(request):
    error=''
    initial_dict = {
        'idcheckimg': request.user.id,
    }
    user_id = initial_dict
    if request.method == 'POST':
        form = Images(request.POST, request.FILES,initial=initial_dict)

        if form.is_valid():
            form.save()
            return redirect('home')

        else:
            error = 'error'

    else:
        form = Images(initial=initial_dict)


    data = {
        'form': form,
        'error': error,
        'user_id':user_id

    }

    return render(request, 'main/addimage.html', data)
