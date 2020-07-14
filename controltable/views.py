from django.http import *
from django.utils import timezone
from django.shortcuts import render
from django.shortcuts import redirect
from .models import ControlTable


def ekle(request):
    
    if request.method== 'POST':
        q = ControlTable(
           cuet=request.POST.get("cuet"), 
           uet=request.POST.get("uet"), 
           atolye=request.POST.get("atolye"), 
           ca=request.POST.get("ca"), 
           kontrolNoktasi=request.POST.get("kontrolNoktasi"), 
           kritiklik=request.POST.get("kritiklik"), 
           kontrolMetod=request.POST.get("kontrolMetod"),
           frekans=request.POST.get("frekans"),
       )

        q.save()

        

    return render(request,'ekle.html')