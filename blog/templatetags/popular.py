from django import template
from blog.models import Post

register = template.Library()


@register.inclusion_tag('blog/popular.html')
def show_popular(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]
    return {'posts': posts}