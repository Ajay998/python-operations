from django.shortcuts import render
import datetime
# Create your views here.

def geeks_views(request):
    context = {
        "data": "Gfg is the best",
        "list": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    context2 = {
        "first_name": "Naveen",
        "last_name": "Arora",
    }
    context3 = {
        "data1":99,
        "data2":101

    }
    return render(request,"geeks.html",{'context':context,'context2':context2,'context3':context3})

def template_filter(request):
    context = {
        "data":1,
        "data2":"This is to remove space",
        "data3" : "Thursday 03, Dec 2012",
        "data4" : ["Coffe","is","good"],
        "data5" : datetime.datetime.now()
    }

    return render(request,"filters.html",{'context':context})