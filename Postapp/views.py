from django.shortcuts import render
from .models import Post
from .forms import PostForm

# Create your views here.

def index(request):
	return render(request, 'index.html')

def posts(request):
	queryset = Post.objects.filter(author=request.user).all()
	context = {"posts": queryset, "form":PostForm}
	return render(request, 'post.html', context=context)

