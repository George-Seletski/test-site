from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    content = models.TextField(blank=True, verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data of publishing')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Date of upadte')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Photo')
    is_published = models.BooleanField(default=True, verbose_name='Published')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Category')

    #id -INT
    #title -VARCHAR
    #content -TEXT
    #created_at - DATETIME
    #updated_at - DATETIME
    #photo - IMAGE
    #is_published - BOOLEAN

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("view_news", kwargs={"news_id": self.pk})
    

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-created_at']
    
class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Name of category")
    
    def get_absolute_url(self):
        return reverse("category", kwargs={"category_id": self.pk})
    

    def __str__(self):
        return self.title
    
        
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'
        ordering = ['title']
