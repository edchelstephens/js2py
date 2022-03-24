from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def env_value():
    return "localhost"