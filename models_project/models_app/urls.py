from django.urls import path
from . import views
urlpatterns = [
    path('datas/',views.musician,name="datas")
]