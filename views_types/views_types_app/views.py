from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Geeksmodel
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .forms import GeeksForm
from django.urls import reverse
# Create your views here.
def func_views(request):
    context = {}
    # add the dictionary during initialization
    context["dataset"] = Geeksmodel.objects.all()
    return render(request, "geeksmodel_list.html", context)

def create_view(request):
    context = {}
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)


def retreive_view(request):
    context = {}
    context["dataset"] = Geeksmodel.objects.all()
    return render(request, "list_view.html", context)


def detail_view(request, id):
    context = {}
    context["data"] = Geeksmodel.objects.get(id=id)
    return render(request, "detail_view.html", context)

def update(request, id):
  mymember = Geeksmodel.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    title = request.POST.get('title')
    description = request.POST.get('description')
    member = Geeksmodel.objects.get(id=id)
    member.title = title
    member.description = description
    member.save()
    return HttpResponseRedirect(reverse('retreive_view'))

def delete(request, id):
  member = Geeksmodel.objects.get(id=id)
  print("Get id: "+str(member))
  member.delete()
  return HttpResponseRedirect(reverse('retreive_view'))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  title = request.POST['title']
  description = request.POST['description']
  member = Geeksmodel(title=title, description=description)
  member.save()
  return HttpResponseRedirect(reverse('retreive_view'))


######################Class based view #####################
class ClassviewList(ListView):
    model = Geeksmodel
class ClassviewCreate(CreateView):
    model = Geeksmodel
    fields = ['title', 'description']

class ClassDetailView(DetailView):
    model = Geeksmodel

class ClassUpdateView(UpdateView):
    model = Geeksmodel
    fields = [
        "title",
        "description"
    ]
    success_url = "/"

class ClassDeleteView(DeleteView):
    model = Geeksmodel
    success_url = "/class_views/"
