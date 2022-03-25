from django.contrib import admin

from blog.models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display = ('name',)   


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display = ('title', 'slug', 'create_date')
    search_fields = ['title', 'body']
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)