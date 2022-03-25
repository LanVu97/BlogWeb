from django.shortcuts import get_object_or_404, render
from django.shortcuts import  render, redirect


from django.contrib import messages

from blog.models import Post



def blog_detail(request, category_slug, blog_slug):
    content ={}
    # get post
    
    post = get_object_or_404(Post, slug=blog_slug)
    # get catagory
    # get author
    content['post'] = post
    return render (request, 'blog/detail.html',content)