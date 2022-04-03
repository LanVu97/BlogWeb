
from django.contrib import admin

from blog.models import Category, Comment, Post
from blog.forms import CommentAdminForm

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display = ('name',)   


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display = ('title', 'slug', 'create_date')
    search_fields = ['title', 'body']

class CommentAdmin(admin.ModelAdmin):
    
    list_display = ('__str__', 'parent', 'created')
    search_fields = ['created ', 'author']

    form = CommentAdminForm
    class Media:
        js = (
            'js/chained-area.js',
        )

    # my_id_for_formfield = None
    # def get_form(self, request, obj=None, **kwargs):
    #     if obj:
    #         self.my_id_for_formfield = obj.id
    #     return super(CommentAdmin, self).get_form(request, obj, **kwargs)

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "parent":
    #         # s = db_field.post
    #         # parent_id = request.resolver_match.kwargs['object_id']
    #         # post = request._obj_
    #         obj = self.get_object(request, self.my_id_for_formfield)
    #         if obj  is not None:

    #         # obj = self.get_object(request, parent_id)
    #             post = obj.post
    #         # print('this is a ......'+ parent_id)
    #             kwargs["queryset"] = Comment.objects.filter(post__exact= post)
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)


    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)