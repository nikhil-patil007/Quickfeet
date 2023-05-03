from django.forms import ModelForm
from game.models import *
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields  = ('contain',)
        widgets = {
            'contain' : forms.TextInput(attrs={'class':'form-control'}),
        }

