from django.shortcuts import render, redirect
from django.views import View
from akun.models import Users
from modul.models.modul import Module, Pelajaran
from modul.models.user import Enroll, UserLatihan, UserPelajaran

context = {}
# Create your views here.
class index(View):
    def get(self, request, slug=None):
        if not slug:
            context["kelas"] = Module.objects.all()
            return render(request, 'modul/index.html', context)

        else:
            module = Module.objects.get(slug=slug)
            enroll = Enroll.objects.filter(user=request.user, kelas=module)
            lesson = UserPelajaran.objects.filter(user=request.user, kelas=module)
            if not enroll.exists():
                Enroll.objects.create(user=request.user, kelas=module)
                return redirect("modul:koridor", slug=slug)
            context["user"] = Users.objects.get(user=request.user)
            context["kelas"] = module
            context["enroll"] = enroll[0]
            context['history'] = enroll.first() if enroll.exists() else None
            context["pelajaran"] = str(lesson.filter(isdone=True).count()) + " / " + str(Pelajaran.objects.filter(module=module).count())
            context['latihan']      = UserLatihan.objects.filter(kelas=module, user=request.user)
            return render(request, 'modul/koridor.html', context)

def koridor(request, slug):
    pass