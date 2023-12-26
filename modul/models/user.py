from django.db import models
from django.contrib.auth.models import User as user_root
Language = [('EN', 'English'),('JP', 'Japan'),('SA', 'Arab'),('CN', 'China')]


class Enroll(models.Model):
    user        = models.ForeignKey(user_root, blank=True, null=True,on_delete=models.CASCADE, related_name="user_course_user")
    kelas       = models.ForeignKey("modul.Module",blank=True, null=True,on_delete=models.CASCADE, related_name="user_kelas")
    pelajaran   = models.ForeignKey("modul.Pelajaran",blank=True, null=True,on_delete=models.CASCADE, related_name="user_history_pelajaran") #mendapat histori pelajaran
    bab_kelas   = models.ForeignKey("modul.Bab",blank=True, null=True,on_delete=models.CASCADE, related_name="user_history")                  # mendapat histori bab
    tanggal     = models.DateField(auto_now_add=True)
    finish      = models.BooleanField(default=False)
    like        = models.IntegerField(default=0)
    feed        = models.CharField(blank=True, null=True, max_length=225)
    feedback    = models.CharField(blank=True, null=True, max_length=225)
    enroll      = models.BooleanField(default=False)
    def __str__(self):
        return "{} take {}".format(self.user, self.kelas)
    def lesson(self):
        return UserPelajaran.objects.filter(userCourse=self)
    def percent(self):
        lesson = UserPelajaran.objects.filter(userCourse=self)
        bab = UserBab.objects.filter(userCourse=self)
        return round(((lesson.filter(isdone=True).count()+bab.filter(isdone=True).count())/(lesson.count()+bab.count()))*100)

# lesson yang sudah dikerjakan
class UserPelajaran(models.Model):
    user        = models.ForeignKey(user_root, blank=True, null=True,on_delete=models.CASCADE, related_name="user_lesson_user")
    kelas       = models.ForeignKey("modul.Module",blank=True, null=True,on_delete=models.CASCADE, related_name="user_kelas_lesson")
    bab_kelas   = models.ForeignKey("modul.Bab",blank=True, null=True,on_delete=models.CASCADE, related_name="user_bab_kelas_lesson")
    pelajaran   = models.ForeignKey("modul.Pelajaran",blank=True, null=True,on_delete=models.CASCADE, related_name="user_pelajaran")
    userCourse  = models.ForeignKey(Enroll,blank=True, null=True,on_delete=models.CASCADE, related_name="usercourse_lesson")
    isdone      = models.BooleanField(default=False)
    question    = models.CharField(max_length=225, blank=True, null=True)
    answer      = models.CharField(max_length=225, blank=True, null=True)
    tgl         = models.DateField(auto_now_add=False, blank=True, null=True)
    def __str__(self):
        return "{} take {} by {}".format(self.id, self.user, self.pelajaran)
    
class UserBab(models.Model):
    user        = models.ForeignKey(user_root, blank=True, null=True,on_delete=models.CASCADE, related_name="user_bab_user")
    kelas       = models.ForeignKey("modul.Module",blank=True, null=True,on_delete=models.CASCADE, related_name="user_kelas_bab")
    bab_kelas   = models.ForeignKey("modul.Bab",blank=True, null=True,on_delete=models.CASCADE, related_name="userbab_bab")
    userCourse  = models.ForeignKey(Enroll,blank=True, null=True,on_delete=models.CASCADE, related_name="usercourse_bab")
    isdone      = models.BooleanField(default=False)
    tgl         = models.DateField(auto_now_add=False, blank=True, null=True)
    def __str__(self):
        return "{} take {} by {}".format(self.id, self.user, self.bab_kelas)


#vocab yang sudah di kerjakan
class UserVocab(models.Model):
    user        = models.ForeignKey(user_root, blank=True, null=True,on_delete=models.CASCADE, related_name="user_vocab_user")
    vocab       = models.ForeignKey("modul.VocabGroup", blank=True, null=True,on_delete=models.CASCADE, related_name="vocab")
    level       = models.IntegerField(default=0)
    benar       = models.IntegerField(default=0)
    salah       = models.IntegerField(default=0)
    isdone      = models.BooleanField(default=False)
    def __str__(self):
        return "{}-{}".format(self.user, self.vocab)
    
#games yang sudah di selesaikan
class UserGames(models.Model):
    user        = models.ForeignKey(user_root, blank=True, null=True,on_delete=models.CASCADE, related_name="user_games_user")
    games       = models.ForeignKey("modul.Games",blank=True, null=True,on_delete=models.CASCADE, related_name="Usergames_Games")
    kelas       = models.ForeignKey("modul.Module",blank=True, null=True,on_delete=models.CASCADE, related_name="Usergames_kelas")
    bab_kelas   = models.ForeignKey("modul.Bab",blank=True, null=True,on_delete=models.CASCADE, related_name="userbab_games")
    right       = models.IntegerField(default=0) #jumlah benar
    wrong       = models.IntegerField(default=0)  #jumlah salah
    failed      = models.IntegerField(default=0) #jumlah orang yg skip
    def __str__(self):
        return "{} {}{}".format(self.id, self.user, self.games)
    
class UserLatihan(models.Model):
    user        = models.ForeignKey(user_root, blank=True, null=True,on_delete=models.CASCADE, related_name="user_latihan_user")
    kelas       = models.ForeignKey("modul.Module",blank=True, null=True,on_delete=models.CASCADE, related_name="user_kelas_latihan")
    pelajaran   = models.ForeignKey("modul.Pelajaran",blank=True, null=True,on_delete=models.CASCADE, related_name="user_latihan_pelajaran")
    bab_kelas   = models.ForeignKey("modul.Bab",blank=True, null=True,on_delete=models.CASCADE, related_name="user_latihan")
    is_last     = models.BooleanField(default=False)
    is_finish   = models.BooleanField(default=False)
    nilai       = models.IntegerField(blank=True, null=True)
    tanggal     = models.DateTimeField(auto_now_add=True)
    countdown   = models.TimeField(default="00:10:00")
    countdownNow= models.TimeField(default="00:10:00")
    def __str__(self):
        return "{}{}".format(self.user, self.nilai)

    def soal(self):
        return UserQuestion.objects.filter(latihan=self)
    

class UserQuestion(models.Model):
    user        = models.ForeignKey(user_root, blank=True, null=True,on_delete=models.CASCADE, related_name="user_question_user")
    questions   = models.ForeignKey("modul.Soal",blank=True, null=True,on_delete=models.CASCADE, related_name="UserQuestion_Question")
    kelas       = models.ForeignKey("modul.Module",blank=True, null=True,on_delete=models.CASCADE, related_name="UserQuestion_kelas")
    bab_kelas   = models.ForeignKey("modul.Bab",blank=True, null=True,on_delete=models.CASCADE, related_name="userbab_Question")
    latihan     = models.ForeignKey(UserLatihan,blank=True, null=True,on_delete=models.CASCADE, related_name="user_latihan")
    selected    = models.CharField(max_length=225, blank=True, null=True)
    right       = models.BooleanField(default=False)
    tanggal     = models.DateField(auto_now_add=True)
    def __str__(self):
        return "{} {}{}".format(self.id, self.user, self.questions)
    