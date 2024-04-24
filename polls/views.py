from django.shortcuts import render
from django.http import HttpResponse
from .models import City

def index(request):
    zh='中国'
    en='China'
    lvel='2'
    return render(request,'display.html',{'name_zh':zh,'name_en':en,'lvl':lvel})
    # return HttpResponse("Hello, world. You're at the polls index.")

def display_city(request):

    city_list = City.objects.all()
    print('000000000000000',city_list,type(city_list))
    print('000000000000001',city_list[0].name_en,type(city_list))

    return render(request,'city.html',{'city_list':city_list})
    # return HttpResponse(city_list)