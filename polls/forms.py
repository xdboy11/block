from django import forms 
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields

from .models import Comment
from django.forms import ModelForm, TextInput, Textarea, widgets, Select

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["title", "content"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите тему'
            }),
            "content": Textarea(attrs={
                'class':'form-control',
                'placeholder': 'введите ваш комментарий'
            }),
        }

from .models import Post, Profile

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "author", "body")
        widgets = {
            "title": forms.TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Введите тему',    
            }),
            "author": forms.TextInput(attrs = {
                'class': 'form-control',
                'value': '',
                'id': 'elder',
                #'type':'hidden',
            }),
            "body": forms.Textarea(attrs = {
                'class': 'form-control',
            }),
        }
        
        

class EditorForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "body")
        widgets = {
            "title": forms.TextInput(attrs = {'class': 'form-control'}),
            "body": forms.Textarea(attrs = {'class': 'form-control'}),
        }

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'facebook_url', 'instagram_url')
        widgets = {
            "bio":forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Кратко о себе'
            }),
            "website_url":forms.TextInput(attrs={
                'class': 'form-control',
            }),
            "instagram_url":forms.TextInput(attrs={
                'class': 'form-control',
            }),
            "facebook_url":forms.TextInput(attrs={
                'class': 'form-control',
            }),
            
        }
