from django.contrib import admin
from .models import News,Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')  # links to models
    search_fields = ('title', 'content')  # filds for searching


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')  # links to models
    search_fields = ('title',)  # filds for searching


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

