from django import template
from website.models import Banner, Links, SiteSetting
from django.conf import  settings
register = template.Library()

@register.inclusion_tag('banner.html')
def show_banners():
    banner_list = Banner.objects.all()
    return {'banner_list': banner_list}

@register.inclusion_tag('footer.html')
def show_footer():
    link_list = Links.objects.all()
    settings = SiteSetting.objects.values('copyright', 'beiancode').first()
    return {'link_list': link_list, 'settings': settings}