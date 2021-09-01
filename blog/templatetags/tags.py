from django import template
from blog.models import Tag

register = template.Library()


@register.inclusion_tag('blog/tags.html')
def show_tags(class_tag='s-content__tag-list'):
    tags = Tag.objects.all()
    return {'tags': tags, 'class_tag': class_tag}


@register.inclusion_tag('blog/tags_cloud.html')
def get_tags():
    tags = Tag.objects.all()
    return {'tags': tags}
