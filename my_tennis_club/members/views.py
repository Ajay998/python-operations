from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
def members(request):
    template = loader.get_template("my_first.html")
    return HttpResponse(template.render())
# Create your views here.
def get_members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))