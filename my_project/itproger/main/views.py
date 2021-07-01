from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from .models import *

# Create your views here.

def index(request):
    return render(request,'main/base.html')

def create(request):
    if request.method == 'POST':
        if request.POST.get('name')!='' and request.POST.get('age')!='':
            name = request.POST.get('name')
            age = request.POST.get('age')
            obj = Create.objects.create(name=name,age=age)
    return render(request,'main/create.html')

def read(request):
    if request.method == 'POST':
        obj = Create.objects.filter(name=request.POST.get('name'))
        my_id = obj.values()[0]['id']
        my_name = obj.values()[0]['name']
        my_age = obj.values()[0]['age']
        return render(request,'main/read.html',{'id':my_id,'name':my_name,'age':my_age})
    return render(request,'main/read.html')

def update(request):
    if request.method == 'POST':
        obj = Create.objects.filter(name=request.POST.get('name'))
        if obj:
            obj.values()[0]['name'] = request.POST.get('newname')
            obj.values()[0]['age'] = request.POST.get('newage')
            my_id = obj.values()[0]['id']
            oldname = obj.values()[0]['name']
            oldage = obj.values()[0]['age']
            newname = request.POST.get('newname')
            newage = request.POST.get('newage')
            for ob in obj:
                ob.name = newname
                ob.age = newage
            ob.save()
            return render(request,'main/update.html',{'newname':newname,'newage':newage,'id':my_id,'oldname':oldname,'oldage':oldage})
    return render(request,'main/update.html')

def delete(request):
    name=''
    if request.method == 'POST':
        obj = Create.objects.filter(name=request.POST.get('name'))
        if obj:
            name = obj.values()[0]['name']
            obj.delete()
    return render(request,'main/delete.html',{'name':name})
