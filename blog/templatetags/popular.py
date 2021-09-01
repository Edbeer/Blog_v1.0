from django import template
from blog.models import Post

register = template.Library()


@register.inclusion_tag()