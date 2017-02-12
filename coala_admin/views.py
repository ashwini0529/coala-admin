from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Blog
def index(request):
	context = {
	'blogs' : Blog.objects.all()
	}
	return render(request, 'coala_admin/index.html', context)
def reviewBlog(request, blog_id):
	context = {
	'blog' : Blog.objects.get(id=int(blog_id))
	}
	#Will implement Http404 if blog does not exists.
	return render(request, 'coala_admin/blog.html', context)
# Create your views here.
