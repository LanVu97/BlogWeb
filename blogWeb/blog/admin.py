from django.contrib import admin

from blog.models import Category, Post

# Register your models here.
admin.site.register(Category)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'create_date')
    search_fields = ['title', 'body']
    

admin.site.register(Post, PostAdmin)