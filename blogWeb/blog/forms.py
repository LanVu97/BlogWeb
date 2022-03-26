from django import forms

from blog.models import Post
# Create your forms here.
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'category', 'image', 'body')
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = ''