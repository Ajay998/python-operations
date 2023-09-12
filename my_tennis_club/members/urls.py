from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('get_members/',views.get_members,name='get_members')
]