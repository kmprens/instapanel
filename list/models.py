from django.db import models
from django.urls import reverse
class Insta(models.Model):
    kuladi = models.CharField(max_length=200, verbose_name='Kullanıcı Adı')
    takipci = models.CharField(max_length=200, verbose_name='Takipçi')
    takip = models.CharField(max_length=200, verbose_name='Takip')
    paylasim = models.CharField(max_length=200, verbose_name='Gönderi')
    kaydetmetarihi=models.DateTimeField(verbose_name='Kaydetme Tarihi')
    prikuladi=models.CharField(max_length=200, verbose_name='Kullanıcı Adı')
    profilresmi=models.CharField(max_length=200, verbose_name='Profil Resmi')




    def __str__(self):
        return self.kuladi




    def get_absolute_url(self):
        return reverse('detail',kwargs={'id':self.id})
    def get_delete_url(self):
        return reverse('delete', kwargs={'id': self.id})









