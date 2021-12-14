from django import template
from website.models import Banner
from django.conf import  settings
register = template.Library()

@register.inclusion_tag('banner.html')
def show_banners():
    banner_list = Banner.objects.all()
    return {'banner_list': banner_list}