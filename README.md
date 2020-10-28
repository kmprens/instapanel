# instapanel
İnstagramın sayfasına istek gönderilerek gelen datayı parçalara ayırarak Takipçi,takip edilen ve gönderi sayısını veritabanına kaydeder.
Bir kere okutulan kullanıcı havuza kaydedilir ve crontablar ile düzenli olarak her gün veriler çekilir ve ileri düzeyde charts kütüphanesi ile
istatistik grafik dökümü alınabilir. 

İçerisinde twitter apisi ile yazılmış, twitter sosyal medya asistanı da vardır.

/////KURULUM//////

1- git clone https://github.com/kmprens/instapanel

2- virtual aktif edilecek.

3- pip install -r requirements.txt ile kütüphaneler kurulacak.

4- python manage.py makemigrations 

5- python manage.py migrate

6- python manage.py runserver

////////////////////

Şinasi ÇEKEMCİ
