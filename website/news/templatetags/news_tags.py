from atexit import register
from django import template

from news.models import Category

register = template.Library()

@register.simple_tag
def get_categories(): #function return tag
    return Category.objects.all()
