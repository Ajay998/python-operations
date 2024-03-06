from django.urls import path
from . import views


urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('members1/',views.members_styling,name='members_styling'),
    path('members1/details/<int:id>', views.details_styling, name='details_styling'),
]