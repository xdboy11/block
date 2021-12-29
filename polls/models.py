from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Article (models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    
    def __str__(self):
        return self.title

class Comment (models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

class Post (models.Model):
    title = models.CharField(max_length = 255)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = RichTextField(blank = True, null = True)
    likes = models.ManyToManyField(User, related_name = "blog_posts")

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse("post-detail", args = (str(self.id)))

class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    bio = models.TextField()
    profile_pic =  models.ImageField(null = True, blank = True, upload_to = "images/profile/")
    website_url = models.CharField(max_length = 255, null = True, blank = True)
    facebook_url = models.CharField(max_length = 255, null = True, blank = True)
    instagram_url = models.CharField(max_length = 255, null = True, blank = True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('posts')
    