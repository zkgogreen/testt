from django.contrib import admin
from kelas.models import UserSchadule, UserMentor, UserMeeting, Schadule, Program, Langganan, Kelas

# Register your models here.
admin.site.register(UserSchadule)
admin.site.register(UserMentor)
admin.site.register(UserMeeting)
admin.site.register(Schadule)
admin.site.register(Program)
admin.site.register(Langganan)
admin.site.register(Kelas)