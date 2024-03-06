from django.urls import path
from . import views
urlpatterns = [
    path('setcookie/',views.setcookie,name='setcookie'),
    path('showcookie/',views.showcookie,name='showcookie')
]