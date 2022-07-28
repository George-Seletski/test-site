from django import forms
from .models import Category, News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control" }),
            'content': forms.Textarea(attrs={"class": "form-control"}),
            'is_published': forms.CheckboxInput(attrs={"class": "form-check-input"}),
            'category': forms.Select(attrs={"class": "form-select"}),
            
            
        }
        
    '''title = forms.CharField(max_length=150, label='The title of the news:',
                            widget=forms.TextInput(attrs={
                                "class": "form-control", }))
    
    content = forms.CharField(label='Content of the news:', required=False,
                              widget=forms.Textarea(attrs={
                                  "class": "form-control"}))
    
    is_published = forms.BooleanField(label='Published:', initial=True, widget=forms.CheckboxInput(
        attrs={
            "class": "form-check-input"}))
    
    category = forms.ModelChoiceField(empty_label='Choose Category', label='Category:', queryset=Category.objects.all(
    ), widget=forms.Select(attrs={
        "class": "form-select"}))
    '''

