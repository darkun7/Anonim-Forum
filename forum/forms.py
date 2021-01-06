from django import forms
from django.forms import ModelForm
from .models import *

class threadForm(ModelForm):
    class Meta:
        model = thread
        fields = '__all__'
        widgets = {
            'judul' : forms.TextInput(attrs={'class': 'form-control'}),
            'konten' : forms.TextInput(attrs={'class': 'form-control summernote'}),
            'penulis' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class komentarForm(ModelForm):
    class Meta:
        model = reply
        fields = ['komentator', 'komentar','thread_id']
        widgets = {
            'komentator' : forms.TextInput(attrs={'class': 'form-control'}),
            'komentar'   : forms.TextInput(attrs={'class': 'form-control summernote'}),
            'thread_id'  : forms.TextInput(attrs={'style': 'display:none'}),
        }
        labels = {
            "thread_id": "",
        }
