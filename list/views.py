from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Insta
from bs4 import BeautifulSoup as bs
import requests
import re
from .forms import ListForm


# Create your views here.

def list_index(request):
    lists = Insta.objects.all()
    query = request.GET.get('q')
    date1 = request.GET.get('d')
    date2 = request.GET.get('d2')
    if date1 and date2:
        lists = lists.filter(kaydetmetarihi__gte=date1, kaydetmetarihi__lte=date2)

    if query:
        lists = lists.filter(kuladi__icontains=query)
    context = {
        'lists': lists,
    }
    return render(request, 'listindex.html', context)


def listdetail(request, id):
    list = get_object_or_404(Insta, id=id)
    context = {
        'list': list

    }
    return render(request, 'detail.html', context)


def list_create(request):
    uyari = ' '
    if request.method == "POST":
        form = ListForm(request.POST)
        ins = Insta.objects.all()
        posts = Insta()
        if form.is_valid():
            if Insta.objects.filter(kuladi=request.POST.get('kuladi')):
                uyari = "BU KULLANICI ZATEN VERİTABANI HAVUZUNDA KAYITLIDIR."
            else:
                url = 'https://www.instagram.com/' + request.POST.get('kuladi')
                print(url)
                r = requests.get(url)
                soup = bs(r.text, 'html.parser')
                gelen = soup.find(property="og:description")
                metin = str(gelen)

                liste = metin.split()
                resim = soup.find(property="og:image")
                res = str(resim)
                resimyolu = res.split()
                print(resimyolu)

                kontrol = re.findall("\W+[a-z]+\w+\W+[0-9-zA -0-9-Za-z]+\w+\W+\S+[a-z]+", resimyolu[1])
                takipci = re.findall("\d+\S+", liste[1])
                takip = re.findall("\d+", liste[3])
                post = re.findall("\d+\S+", liste[5])

                # ---------------------------------------------------------------------------
                kkontrol = ''
                for i in kontrol:
                    kkontrol = kkontrol + str(i)
                kkontrol = kkontrol.replace('="', "", 1)
                # -------------------------------------------------------------------------

                ktakip = ''
                if takip:
                    for i in takip:
                        ktakip = ktakip + str(i)
                else:
                    ktakip = 0

                # -------------------------------------------------------------------------
                ktakipci = ''
                if takipci:
                    for i in takipci:
                        ktakipci = ktakipci + str(i)
                        kontrol = re.search("", ktakipci)
                        if re.findall("\d+\W+\d+", ktakipci):
                            ktakipci = ktakipci.replace("m", "00000", 1)
                        if re.findall("\d+", ktakipci):
                            ktakipci = ktakipci.replace("m", "000000", 1)
                        if re.findall("\d+\W+\d+", ktakipci):
                            ktakipci = ktakipci.replace("k", "00", 1)
                        if re.findall("\d+", ktakipci):
                            ktakipci = ktakipci.replace("k", "000", 1)

                        ktakipci = ktakipci.replace(".", "", 1)
                        ktakipci = ktakipci.replace(",", "", 1)


                else:
                    ktakipci = 0

                # -------------------------------------------------------------------------

                kpost = ''
                if post:
                    for i in post:
                        kpost = kpost + str(i)
                    kpost = kpost.replace(",", "")
                else:
                    kpost = 0

                # -------------------------------------------------------------------------

                posts.takipci = int(ktakipci)
                posts.takip = int(ktakip)
                posts.kuladi = request.POST.get('kuladi')
                posts.prikuladi = request.POST.get('kuladi')
                posts.paylasim = int(kpost)
                posts.profilresmi = kkontrol
                posts.save()
                return redirect('index')

    else:
        form = ListForm()

    context = {

        'form': form,
        'uyari': uyari,

    }
    return render(request, 'form.html', context)


def list_delete(request, id):
    list = get_object_or_404(Insta, id=id)
    list.delete()
    return redirect('index')


# -------------------------------------------------------------
def istatistik(request):
    ins = Insta.objects.all()
    a = max(int(x.takipci) for x in ins)
    list = get_object_or_404(Insta, takipci=a)
    b = max(int(x.takip) for x in ins)
    lists = get_object_or_404(Insta, takip=b)
    c = max(int(x.paylasim) for x in ins)
    listss = get_object_or_404(Insta, paylasim=c)
    filtre = ins.filter(kuladi__icontains="baybilinen")

    for x in filtre:
        filtre = [x]
    for yaz in filtre:
        print(yaz.kaydetmetarihi)

    context = {

        'enyuksek': a,
        'eytakip': b,
        'eypaylasim': c,
        'list': list,
        'lists': lists,
        'listss': listss,
        'filtre': filtre,

    }

    return render(request, 'istatistik.html', context)


def get_statistic_by_user(request, type):
    from django.db.models import F
    all_users = Insta.objects.all().extra(select={f'{type}': f'CAST({type} AS INTEGER)'},
                                          order_by=[f'{type}']).reverse()
    json_users = []
    for user in all_users.values():
        json_users.append({
            'name': user['kuladi'],
            'y': int(user[type])
        })
    return JsonResponse(json_users, safe=False)


def statistic_charts(request):
    return render(request, 'total_statistics.html')
