from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

appid="c7ce0415da92323388c1b3bf8120a45c"
url="https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=ru&appid="+appid

def index(request):
    if request.method=='POST':
        form=CityForm(request.POST)
        form.save()
    form=CityForm()

    cities=City.objects.all()
    all_cities=[]
    for city in cities:
        res=requests.get(url.format(city.name)).json()
        city_info={
            'city':city.name,
            'pk':city.pk,
            'temp':res['main']['temp'],
            'icon':res['weather'][0]['icon']
        }
        all_cities.append(city_info)
    context={'all_info':all_cities,'form':form}

    return render(request,'weather/index.html',context)

def city_detail(request,pk):
    city=City.objects.get(pk=pk)
    res = requests.get(url.format(city.name)).json()
    city_info={
        'city':city.name,
        'temp':res['main']['temp'],
        'feels_like':res['main']['feels_like'],
        'humidity': res['main']['humidity'],
        'main':res['weather'][0]['main'],
        'wind':res['wind']['speed'],
        'icon':res['weather'][0]['icon']
        }
    context={'info':city_info}
    return render(request,'weather/city_detail.html',context)