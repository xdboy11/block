from django.db import models
from django.db.models import fields
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, request
from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView
from django.urls.base import reverse
from .forms import CommentForm, ProfilePageForm
from .models import Comment, Profile


def about(request):
    return render(request, "about.html")

def home(request):
    return render(request, "home.html")

def otziv(request):
	coments = Comment.objects.order_by('-id')
	print(coments)
	return render(request, 'otziv.html', { 'coments': coments } )

def create(request):
	error = ''
	coments = Comment.objects.order_by('-id')  # Коментарии на этой же страницы
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('create')
		else:
			error = 'Форма была неверной'
	form = CommentForm()
	
	context = {
		"form":form,
		"error":error,
		'coments':coments # Коментарии на этой же страницы
	}
	return render(request, "create.html", context)


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
from .forms import PostForm, EditorForm

class HomeView(ListView):
	model = Post
	template_name = 'post.html'
	ordering = ['-id']

class PostHomeView(DetailView):
	model = Post
	template_name = 'post_details.html'

	def get_context_data(self, **kwargs):
		context = super(PostHomeView, self).get_context_data(**kwargs)
		stuff = get_object_or_404(Post, id = self.kwargs['pk'])
		total_likes = stuff.total_likes()
		liked = False
		if stuff.likes.filter(id = self.request.user.id).exists():
			liked = True
		context['total_likes'] = total_likes
		context['liked'] = liked
		return context
		

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = "add_post.html"

class UpdatePostView(UpdateView):
	model = Post
	form_class = EditorForm
	template_name = "update_post.html"

def likeview(request, pk):
	post = get_object_or_404(Post, id = request.POST.get('post_id'))
	liked = False
	if post.likes.filter(id = request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else:
		post.likes.add(request.user)
		liked = True
	return HttpResponseRedirect(reverse('post-detail', args = [str(pk)]))

class ShowProfilePageView(DetailView):
	model = Profile
	template_name = 'user_profile.html'

	def get_context_data(self, *args, **kwargs):
		context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

		page_user = get_object_or_404(Profile, id = self.kwargs['pk'])
		context["page_user"] = page_user
		return context

class CreateProfilePageView(CreateView):
	model = Profile
	form_class = ProfilePageForm
	template_name = 'create_user_profile.html'
	def form_valid (self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class EditProfilePageView(UpdateView):
	model = Profile
	template_name = 'edit_user_profile.html'
	fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'instagram_url']

	succes_url = reverse_lazy('show_profile_page')
