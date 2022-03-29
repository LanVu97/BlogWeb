from django.db.models import Count
from blog.models import Category, Comment, Post


def get_categories(request):
    """
      The context processor must return a dictionary.
    """
    cateCount = {}
    categories = Category.objects.all()
    
    for cate in categories:
        num = Post.objects.filter(category=cate).count
        cateCount[cate] = num        
   
    return {'cateCount': cateCount}

def getPopularPosts(request):
    posts = Post.objects.annotate(numComment=Count('comments')).order_by('-numComment')
    top_three_posts = posts[:3]
    for i in posts:
      print(i)
      print(i.numComment)

    return {'popularPosts': top_three_posts}