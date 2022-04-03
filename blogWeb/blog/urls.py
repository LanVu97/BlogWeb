from django.urls import path
import blog.views as views

urlpatterns = [
    path('category/<slug:category_slug>/<slug:blog_slug>', views.blog_detail, name='blog_detail'),
    path('category/<slug:category_slug>', views.category, name='category'),
    path('create_blog/', views.create_blog, name='create_blog'),
    path('delete_blog/<slug:blog_slug>', views.delete_blog, name='delete_blog'),
    path('update_blog/<slug:blog_slug>', views.update_blog, name='update_blog'),
    path('parent/<int:post_id>', views.parent_comment_list, name='parent_comment'),
]