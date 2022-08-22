

from msilib.schema import Class
from pyexpat import model
from re import template
from statistics import mode
from tkinter import NE
from unicodedata import category
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import News, Category
from .forms import NewsForm 

class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news_lst = News.objects.first()
        context['title'] = "TITILE"
        context['categories'] = Category.objects.all()
        context['news_last'] = news_lst
        context['news_all'] = News.objects.filter(id__lt = news_lst.id)
        return context
    
    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')
    
class NewsByCategory(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        context['categories'] = Category.objects.all()
        return context
    
    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')
    
class ViewNews(DetailView):
    model = News
    #pk_url_kwarg = 'news_id'
    #template_name = 'news/news_detail.html'
    context_object_name = 'news_item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


 class CreateNews(CreateView):
     form_class = NewsForm
     template_name = 'news/add_news.html'
     success_url = reverse_lazy('home')
    
     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['categories'] = Category.objects.all()
         return context
    

# def index(request):
#     news = News.objects.all()
#     res = '<h1>List of news:</h1>'
#     categories = Category.objects.all()
#     context = {
#         'news': news,
#         'title': 'List of news',
#         'categories':categories,
#     }
#     return render(request, 'news/index.html', context)

# def get_category(request, category_id):
#     news = News.objects.filter(category_id = category_id)
#     categories = Category.objects.all()
#     category = Category.objects.get(pk = category_id)
#     context = {
#         'news': news,
#         'categories': categories,
#         'category':category,
#     }
#     return render(request, 'news/categories.html',context)

# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     categories = Category.objects.all()
#     return render(request, 'news/view_news.html', {"news_item": news_item, 'categories': categories,})
    
# def add_news(request):
#      categories = Category.objects.all()
#      if request.method == 'POST':
#          form = NewsForm(request.POST, request.FILES)
#          if form.is_valid():
#              # print(form.cleaned_data)
#              # news = News.objects.create(**form.cleaned_data)
#              news = form.save()
#              return redirect(news)
            
#      else:
#          form = NewsForm()
#      return render(request, 'news/add_news.html', {'form': form, 'categories': categories,})


def about(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'news/about.html', context)
