from django.shortcuts import redirect, render
from akun.models import Users
from modul.models.modul import Pelajaran

def index(request):
    context = {
        'user':Users.objects.filter(teacher=False).count(),
        'teacher':Users.objects.filter(teacher=True).count(),
        'module':Pelajaran.objects.all().count()
    }
    return render(request, 'index.html', context)

def home(request):
    context = {

    }
    return render(request, 'home/index.html', context)