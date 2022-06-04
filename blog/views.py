from django.shortcuts import render
from .models import BlogPost

def home(request):
  posts=BlogPost.objects.all()
  context={'posts': posts}
  return render(request,'home.html',context)

