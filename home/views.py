from django.shortcuts import render, HttpResponse
from list.models import Insta


def homeview(request):
    lists = Insta.objects.all()
    query = request.GET.get('q')
    if query:
        lists = lists.filter(kuladi__icontains=query)
    context = {
        'lists': lists,
    }
    return render(request, 'home.html', context)
