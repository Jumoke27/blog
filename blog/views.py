from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.views.generic import TemplateView
# Create your views here.
def post_list(request):
	# posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	template = 'blog/post_list.html'
	posts=Post.objects.all()
	return render(request, 'blog/post_list.html', {"posts":posts})


def about(request):
	# posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	template = 'blog/aboutus.html'
	return render(request, template)	

def single_post(request, ppk):
	post=Post.objects.get(id=ppk)
	template = 'blog/singlepost.html'
	return render(request, template, {"post":post})	
