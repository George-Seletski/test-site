from turtle import title
from django import forms
from django.core.exceptions import ValidationError

from .models import Category, News
import re

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        # fields = ['title', 'content', 'is_published', 'category', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control" }),
            'content': forms.Textarea(attrs={"class": "form-control"}),
            'is_published': forms.CheckboxInput(attrs={"class": "form-check-input"}),
            'category': forms.Select(attrs={"class": "form-select"}),
        }
        
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError("Title can't begin with  numbers")
        return title
        

