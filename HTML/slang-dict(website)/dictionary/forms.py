from django import forms

from .models import Baslik

class PostForm(forms.ModelForm):

    class Meta:
        model = Baslik
        fields = ('kelime', 'anlami',)

