from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True, verbose_name='URL')

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True, verbose_name='URL')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True, verbose_name='URL')
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

