from email.mime import image
from django.db import models
from django.urls import reverse

from account.models import User
# Import slugify to generate slugs from strings
from django.utils.text import slugify 
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):                           
        return self.name

class Post(models.Model):
    author =  models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to ='blogs')
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    
    class Meta:
        ordering = ['-create_date']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs) 

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'blog_slug': self.slug, 'category_slug':self.category.slug })

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies',on_delete=models.CASCADE)

    class Meta:
        # sort comments in chronological order by default
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {}'.format(self.author.username)