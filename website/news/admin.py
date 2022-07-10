from turtle import title
from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')  # links to models
    search_fields = ('title', 'content')  # filds for searching


admin.site.register(News, NewsAdmin)
