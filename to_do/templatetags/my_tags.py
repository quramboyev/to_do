from django import template
from django.utils.html import mark_safe

register = template.Library()

def test(v: str):
    return [i for i in v]

register.filter('test', test)

@register.filter('new_filter')
def new(obj):
    html_code = f"<img src='{ obj.img.url }'></img>"
    return mark_safe(html_code)