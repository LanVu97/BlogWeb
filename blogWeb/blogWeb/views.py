from django.shortcuts import render

from blog.models import Post

def home(request):
    content = {}
    try:
        posts = Post.objects.all()
    except:
        print('error: cant get all posts')
    content['posts'] = posts
    return render(request, 'index.html', content)