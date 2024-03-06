from django.urls import path
from . import views
from .views import ClassviewList
from .views import ClassviewCreate
from .views import ClassDetailView
from .views import ClassUpdateView
from .views import ClassDeleteView

urlpatterns =[
    path('func_views/', views.func_views, name='func_views'),
    path('create_view/',views.create_view,name='create_view'),
    path('retreive_view/',views.retreive_view,name='retreive_view'),
    path('detail_view/<int:id>',views.detail_view,name='detail_view'),
    path('retreive_view/update/<int:id>',views.update,name='update'),
    path('retreive_view/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('retreive_view/delete/<int:id>', views.delete, name='delete'),
    path('retreive_view/add/', views.add, name='add'),
    path('retreive_view/add/addrecord/', views.addrecord, name='addrecord'),
    ############### Class based views urls ################
    path('class_views/',ClassviewList.as_view()),
    path('class_views_create/',ClassviewCreate.as_view()),
    path('class_views_detail/<pk>/',ClassDetailView.as_view()),
    path('class_views_update/<pk>/update',ClassUpdateView.as_view()),
    path('class_views_delete/<pk>/delete',ClassDeleteView.as_view())
]