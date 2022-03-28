

from django.shortcuts import get_object_or_404, render
from django.shortcuts import  render, redirect


from django.contrib import messages

from blog.models import Category, Post
from blog.forms import PostForm


def blog_detail(request, category_slug, blog_slug):
    content ={}    
    post = get_object_or_404(Post, slug=blog_slug)

    content['post'] = post
    return render (request, 'blog/detail.html',content)

def category(request, category_slug):
    content ={}
    cate_name = Category.objects.get(slug= category_slug).name
    posts = Post.objects.filter(category__slug=category_slug)
    content['category_posts'] = posts
    content['cate_name'] = cate_name
    return render (request, 'blog/category.html',content)

def create_blog(request):
    context = {}
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    context['form']= form
    return render (request, 'blog/create.html',context)

def delete_blog(request, blog_slug):
    obj = get_object_or_404(Post, slug = blog_slug)
 
    if request.method =="POST":
        # delete object
        obj.delete()
        return redirect('home')   
   

def update_blog(request, blog_slug):
    context ={}
    obj = get_object_or_404(Post, slug = blog_slug)
    if request.method == "POST":
        
        form = PostForm(request.POST,  request.FILES, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
         form = PostForm(instance = obj)
    # add form dictionary to context
    context["form"] = form
    return render(request, 'blog/update_blog.html', context)