from django.contrib import admin
from .models import News,Category
from django.utils.safestring import mark_safe

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')  # links to models
    search_fields = ('title', 'content')  # filds for searching
    fields = ( 'title', 'category', 'content', 'photo', 'get_photo', 'is_published','views', 'created_at',
              'updated_at')
    readonly_fields = ('get_photo', 'views', 'created_at','updated_at')
    
    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return '-'
    get_photo.short_description = 'photo'
        

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')  # links to models
    search_fields = ('title',)  # filds for searching


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'News manager'
admin.site.site_header = 'News manager'
