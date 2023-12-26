from kelas.models import Kelas, Schadule, UserMeeting
from transaksi.models import TransaksiGuru, Transaksi
from config.models import Setting
from akun.models import Teacher
from kelas.models import Program

from transaksi.utils import midtrans, purchase

from django.db.models import F
import datetime
x = datetime.datetime.now()
setting = Setting.objects.all().first()

Language = [('EN', 'English'),('JP', 'Japan'),('SA', 'Arab'),('CN', 'China')]
jam     = [(0,'07:30'),(1,'09:00'),(2,'10:30'),(3,'13:00'),(4,'14:30'),(5,'16:00'),(6,'18:30'),(7,'20:00')]
jadwal = [(0, 'senin,  rabu, jum\'at'),(1, 'selasa,  kamis, sabtu'),(2, 'jum\'at,  sabtu, minggu')]

def fetchday(tanggal, hari):
    # Convert the string to a datetime.date object
    tanggal = datetime.datetime.strptime(tanggal, '%Y-%m-%d').date()

    pilih_hari = [0, 2, 4] if hari == 0 else [1, 3, 5] if hari == 1 else [4, 5, 6]
    tanggal_hari_tertentu = []
    i = 1
    while i <= 30:
        if tanggal.weekday() in pilih_hari:  # Senin=0, Rabu=2, Jumat=4
            tanggal_hari_tertentu.append(tanggal)
            i = i + 1
        # Tambahkan 1 hari ke tanggal
        tanggal += datetime.timedelta(days=1)

    return tanggal_hari_tertentu

def ambilKelas(transaksi, kelas):
    meeting = UserMeeting.objects.create(mentor=kelas.mentor,user=transaksi.user ,kelas=kelas, program=kelas.level,start=kelas.mulai ,meetremain=kelas.program.pertemuan)
    TransaksiGuru.objects.create(user=kelas.mentor, jumlah=kelas.program.discount * setting.komisi_teacher / 100)
    Teacher.objects.filter(user=kelas.mentor).update(pendapatan=F('pendapatan'))
    return meeting

def buatKelas(user, program, jam, jadwal, mulai):
    kelas   = Kelas.objects.create(mentor=user ,bahasa='EN' ,program=program,time=jam,mulai=mulai ,jadwal=jadwal)
    for day in fetchday(kelas.mulai, kelas.jadwal):
                Schadule.objects.create(room=kelas, mentor=user, tanggal=day, program=kelas.program)
    return kelas

def upgradeKelas(request, id):
    program = Program.objects.get(id=id)
    transaksi = purchase(user=request.user, program=program)
    
    # Transaksi.objects.create(user=request.user, )
    price = program.biaya
    ref_id = transaksi.id
    url, SessionID = midtrans(request, price, ref_id)
    # url, SessionID = pay(request, product, price, ref_id)
    transaksi.SessionID = SessionID
    transaksi.save()
    return url

def confirmUpgrade(request, transaksi):
    program = Program.objects.get(id=transaksi.program.id)
    nextmonth = x.replace(month=(x.month + program.durasi) % 12 + 1)

    if nextmonth.month == 1:
        nextmonth = nextmonth.replace(year=nextmonth.year + 1)
    UserMeeting.objects.create(user=request.user, transaksi=transaksi, program=program, end=nextmonth, meetremain=program.pertemuan)
    

    


