from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name="index"),
    path('modul/<str:slug>', views.index.as_view(), name="koridor"),
    path('modul/subscribe/<str:slug>', views.index.as_view(), name="subscribe"),
]