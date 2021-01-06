from django.db import models

# Create your models here.
class thread(models.Model):
    judul = models.CharField(max_length=200)
    konten = models.TextField(null=True)
    penulis = models.CharField(max_length=64, null=True)
    tanggaldibuat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul

class reply(models.Model):
    thread_id = models.ForeignKey(thread ,null=True, on_delete=models.SET_NULL)
    komentator = models.CharField(max_length=64, null=True)
    komentar = models.TextField(null=True)
    tanggalkomentar = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.thread_id)+":"+str(self.komentator)+":"+str(self.komentar)
