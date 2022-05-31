from django.shortcuts import render
from django.db.models import Q
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    content = {}
    post_list =[]
    try:
        post_list = Post.objects.all().order_by("-create_date")
    except:
        print('error: cant get all posts')


    # getting the desired page number from url
    page = request.GET.get('page')
    # creating a paginator object
    paginator = Paginator(post_list, 6) # 6 posts per page

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        posts = paginator.page(paginator.num_pages)

    content['posts'] = posts
    return render(request, 'index.html', content)

def search(request):
    search_post = request.GET['q']
    content = {}
    if search_post:
        post_list = Post.objects.filter(Q(title__icontains=search_post) | Q(body__icontains=search_post))
    else:
    # If not searched, return default posts
        post_list = Post.objects.all().order_by("-create_date")

    # getting the desired page number from url
    page = request.GET.get('page')
    # creating a paginator object
    paginator = Paginator(post_list, 6) # 6 posts per page

    try:
        # returns the desired page object
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        posts = paginator.page(paginator.num_pages)


    content['posts'] = posts

    return render(request, 'blog/searchResult.html', content)

def contact(request):
     return render(request, 'contact.html')
