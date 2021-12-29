from django.contrib import admin
from django import forms
from django.db import models
from django.forms import widgets
from .models import Article
from .models import Post
from .models import Profile
from ckeditor.widgets import CKEditorWidget

class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(label = "Описание", widget = CKEditorWidget())
    class Meta:
        model = Article
        fields = '__all__'


class ArticlAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'context')
    form = ArticleAdminForm

admin.site.register(Article, ArticlAdmin)
admin.site.register(Post)
admin.site.register(Profile )

# Register your models here.

