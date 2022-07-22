from hashlib import new
from unicodedata import category
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import News, Category
# Create your views here.


def index(request):
    news = News.objects.all()
    res = '<h1>List of news:</h1>'
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'List of news',
        'categories':categories,
    }
    return render(request, 'news/index.html', context)

def get_category(request, category_id):
    news = News.objects.filter(category_id = category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk = category_id)
    context = {
        'news': news,
        'categories': categories,
        'category':category,
    }
    return render(request, 'news/categories.html',context)

def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {"news_item": news_item})
    
