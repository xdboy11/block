
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from polls.views import about as about
from polls.views import home as home
from polls.views import create as create
from polls.views import otziv as otziv
from polls.views import likeview
from polls.views import HomeView, PostHomeView, UpdatePostView, AddPostView, ShowProfilePageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('home/', home, name = "home"),
    path('create/', create, name = "create"),
    #path('register/', register),
    #path('login/', login),
    path('about/', about, name = "homepage"),
    path('otziv/', otziv, name = "otziv"),
    path('about/', include('django.contrib.auth.urls')),
    path('posts/', HomeView.as_view(), name = "posts"),
    path('posts/<int:pk>', PostHomeView.as_view(), name = "post-detail"),
    path('add_post/', AddPostView.as_view(), name = "add_post"),
    path('posts/edit/<int:pk>', UpdatePostView.as_view(), name = "update_post"),
    path('like/<int:pk>', likeview, name = 'like_post'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name = "show_profile_page"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)