
from blog.models import Category, Post


def get_categories(request):
    """
      The context processor must return a dictionary.
    """
    cateCount = {}
    categories = Category.objects.all()
    for cate in categories:
        num = Post.objects.filter(category=cate).count
        cateCount[cate.name] = num

    for i in cateCount:
        print(i)
    return {'cateCount': cateCount}