# -*- coding: utf-8 -*-
from django import forms
from .models import ArticleImage

class ArticleImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={"allow_multiple_selected": True}), required=False)

    class Meta:
        model = ArticleImage
        fields = '__all__'