
from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    #id -INT
    #title -VARCHAR
    #content -TEXT
    #created_at - DATETIME
    #updated_at - DATETIME
    #photo - IMAGE
    #is_published - BOOLEAN

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-created_at']
    
class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Name of category")

    def __str__(self):
        return self.title
    
        
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'
        ordering = ['title']