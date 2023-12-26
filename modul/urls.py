from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('koridor/<str:slug>', views.koridor, name="koridor"),
]