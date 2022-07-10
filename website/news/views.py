from hashlib import new
from django.shortcuts import render
from django.http import HttpResponse

from .models import News
# Create your views here.


def index(request):
    news = News.objects.all()
    res = '<h1>List of news:</h1>'
    context = {
        'news': news,
        'title': 'List of news'
    }
    return render(request, 'news/index.html', context)
