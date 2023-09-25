from django.shortcuts import render
from django.http import HttpResponse
from .models import Musician
# Create your views here.

def musician(request):
    musican_detail = Musician.objects.all()
    print(musican_detail)
    context = {
        "datas":musican_detail
    }
    return render(request,'base.html',context)
