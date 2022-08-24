from django.shortcuts import render
import requests

def index(request):
    appid="c7ce0415da92323388c1b3bf8120a45c"
    url="https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid="+appid
    city="Minsk"
    res=requests.get(url.format(city)).json()
    city_info={
        'city':city,
        'temp':res['main']['temp'],
        'feels_like':res['main']['feels_like'],
        'humidity': res['main']['humidity'],
        'main':res['weather'][0]['main'],
        'wind':res['wind']['speed'],
        'icon':res['weather'][0]['icon']}
    context={'info':city_info}
    print (res)
    return render(request,'weather/index.html',context)

def news(request):
    return render(request,'weather/news.html')