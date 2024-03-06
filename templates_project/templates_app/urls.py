from django.urls import path
from . import views

urlpatterns = [
    path('geeks/',views.geeks_views,name='geeks_views'),
    path('filter/',views.template_filter,name='template_filter')
]