from django.urls import path
from . import views
urlpatterns = [
    path('sql_datas/',views.student_list,name="sql_datas")
]