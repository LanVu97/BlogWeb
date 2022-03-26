from django.urls import path
import blog.views as views

urlpatterns = [
    path('category/<slug:category_slug>/<slug:blog_slug>', views.blog_detail, name='blog_detail'),
    path('category/<slug:category_slug>', views.category, name='category')
   
]