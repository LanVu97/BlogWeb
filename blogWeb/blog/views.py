from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import  render, redirect


from django.contrib import messages

from blog.models import Category, Comment, Post
from blog.forms import CommentForm, PostForm


def blog_detail(request, category_slug, blog_slug):
    content ={}    
    post = get_object_or_404(Post, slug=blog_slug)
    # list of active parent comments
    comments = post.comments.filter(parent__isnull=True).order_by('-updated')
    if request.method == "POST":
        # comment has been added
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():         
            
            parent_obj = None
            # get parent comment id from hidden input
            try:
                # id integer e.g. 15
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            # if parent_id has been submitted get parent_obj id
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                # if parent object exist
                if parent_obj:
                    # create replay comment object
                    replay_comment = comment_form.save(commit=False)

                    # assign parent_obj to replay comment
                    replay_comment.parent = parent_obj
            # normal comment
            # create comment object but do not save to database
            new_comment = comment_form.save(commit=False)
            # assign ship to the comment
            new_comment.post = post
            new_comment.author = request.user
            # save
            new_comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
            comment_form = CommentForm()

    content['post'] = post
    content['comments'] = comments
    content['comment_form'] = comment_form
    content['category_slug'] = category_slug
    return render (request, 'blog/detail.html',content)

def category(request, category_slug):
    content ={}
    cate_name = Category.objects.get(slug= category_slug).name
    post_list = Post.objects.filter(category__slug=category_slug).order_by("-create_date")

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
    content['category_posts'] = posts
    content['cate_name'] = cate_name
    return render (request, 'blog/category.html',content)
@login_required(login_url='login')
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
    
@login_required(login_url='login')
def delete_blog(request, blog_slug):
    obj = get_object_or_404(Post, slug = blog_slug)
 
    if request.method =="POST":
        # delete object
        obj.delete()
        return redirect('home')   
   
@login_required(login_url='login')
def update_blog(request, blog_slug):
    context ={}
    obj = get_object_or_404(Post, slug = blog_slug)
    if request.method == "POST":
        
        form = PostForm(request.POST,  request.FILES, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
        if form.is_valid():
            form.save()
            return redirect(obj.get_absolute_url())
    else:
         form = PostForm(instance = obj)
    # add form dictionary to context
    context["form"] = form
    return render(request, 'blog/update_blog.html', context)

@login_required(login_url='login')
def parent_comment_list(request, post_id):
    print(post_id)
    comment = Comment.objects.filter(post__id=post_id, parent__isnull=True)
    return JsonResponse({'data': [{'id': k.id, 'author': k.author.username} for k in comment]})

