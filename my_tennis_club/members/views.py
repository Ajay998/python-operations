from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q
def members(request):
    template = loader.get_template("my_first.html")
    return HttpResponse(template.render())
# Create your views here.
def members(request):
    mymembers = Member.objects.all().values()
    first_name = Member.objects.all().values_list('firstname')
    emil_data = Member.objects.filter(firstname='Emil').values()
    emil_tobias_data = Member.objects.filter(Q(firstname='Emil') | Q(firstname='Tobias')).values()
    data_starts_with_l = Member.objects.filter(firstname__startswith = "L").values()
    mydata_contains = Member.objects.filter(firstname__contains='bias').values()
    all_data_order_by_asc = Member.objects.order_by('firstname').values()
    all_data_order_by_desc = Member.objects.all().order_by('-firstname').values()
    multiple_data_order_by = Member.objects.all().order_by('lastname', '-id').values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
        'greetings': 1,
        'first_name':first_name,
        'emil_data':emil_data,
        'emil_tobias_data':emil_tobias_data,
        'data_starts_with_l':data_starts_with_l,
        'mydata_contains':mydata_contains,
        'all_data_order_by_asc':all_data_order_by_asc,
        'all_data_order_by_desc':all_data_order_by_desc,
        "multiple_data_order_by":multiple_data_order_by
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = Member.objects.get(id=id)
    print(mymember)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def members_styling(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members_styling.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details_styling(request,id):
    mymember = Member.objects.get(id=id)
    print(mymember)
    template = loader.get_template('details_styling.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

#################### Function based views ###########################
