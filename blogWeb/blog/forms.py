from django import forms

from blog.models import Comment, Post
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

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('body',)
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs['class'] = 'form-control'
        self.fields['body'].widget.attrs['rows'] = "5"

class CommentAdminForm(forms.ModelForm): 
    
    class Meta:
        model = Comment
        fields = '__all__'
