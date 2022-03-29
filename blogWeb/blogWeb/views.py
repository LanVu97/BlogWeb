from django.shortcuts import render
from django.db.models import Q
from blog.models import Post

def home(request):
    content = {}
    try:
        posts = Post.objects.all()
    except:
        print('error: cant get all posts')
    content['posts'] = posts
    return render(request, 'index.html', content)

def search(request):
    search_post = request.GET['q']
    content = {}
    if search_post:
        posts = Post.objects.filter(Q(title__icontains=search_post) | Q(body__icontains=search_post))
    else:
    # If not searched, return default posts
        posts = Post.objects.all().order_by("-date_created")
    content['posts'] = posts
    return render(request, 'index.html', content)