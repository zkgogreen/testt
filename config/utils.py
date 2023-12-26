from config.models import Setting
from akun.models import Users, Premium
from datetime import datetime, date

def is_date_in_range(request):
    if not request.user.is_authenticated:
        return False
    premium = Premium.objects.filter(user=request.user)
    if not premium.exists():
        return False
    return premium.premium_start <= datetime.now() <= premium.premium_end
    
def beforeRequest(request):
    if request.user.is_authenticated:
        user = Users.objects.filter(user=request.user.id)
        if not user.exists():
            Users.objects.create(user=request.user)

def config(request):

    beforeRequest(request)

    context = {}
    context['config']   = Setting.objects.get()
    context['me']       = Users.objects.get(user=request.user) if request.user.is_authenticated else ''
    context['premium']  = is_date_in_range(request) if request.user.is_authenticated else False
    context['mentorlist']   = Users.objects.filter(teacher=True)
    return context