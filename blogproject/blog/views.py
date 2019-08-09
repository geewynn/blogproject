from django.shortcuts import render
from django.http import HttpResponse
from .models import blog_article
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):

    blog = blog_article.objects.all()
    text = 'Your best blog'
#    context = {'text': text, 'blog': blog, 'user': user}
    if request.method== 'Post':
        usname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=usname, password=pwd)
        if user is not None:
            login(request, user)
            return render(request, 'index.html', {'text': text, 'blog': blog, 'user': user})

    return render(request, 'index.html', {'text': text, 'blog': blog, 'user': None})
def createlog(request):
    newBlog = blog_article()
    newBlog.title = request.POST['title']
    newBlog.author = request.user
    newBlog.blog_content = request.POST['blog_content']
    newBlog.save()
    return render(request, 'index.html', {'text': text, 'blog': blog, 'user': user})
