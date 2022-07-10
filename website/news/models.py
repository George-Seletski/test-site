from calendar import c
from operator import mod
from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)

    #id -INT
    #title -VARCHAR
    #content -TEXT
    #created_at - DATETIME
    #updated_at - DATETIME
    #photo - IMAGE
    #is_published - BOOLEAN

    def __str__(self):
        return self.title
