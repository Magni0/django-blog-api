from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1
    )
    
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts'
    )
    title = models.CharField(max_length=200)
    exerpt = models.TextField(null=True)
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=options, default='published')

    slug = models.SlugField(max_length=200, unique_for_date='published')

    objects = models.Manager() # default
    postobjects = PostObjects() # custom

    class Meta:
        ordering = ('-published', )

    def __str__(self):
        return self.title