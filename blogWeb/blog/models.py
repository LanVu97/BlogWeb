from email.mime import image
from django.db import models

from account.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

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

    def __str__(self):
        return self.title