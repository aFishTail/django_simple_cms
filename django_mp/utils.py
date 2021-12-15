#!/usr/bin/env python
# encoding: utf-8


import logging
import random
import string
from hashlib import sha256

# from django.contrib.sites.models import Site
from django.core.cache import cache

logger = logging.getLogger(__name__)



def get_sha256(str):
    m = sha256(str.encode('utf-8'))
    return m.hexdigest()


def cache_decorator(expiration=3 * 60):
    def wrapper(func):
        def news(*args, **kwargs):
            try:
                view = args[0]
                key = view.get_cache_key()
            except BaseException:
                key = None
            if not key:
                unique_str = repr((func, args, kwargs))

                m = sha256(unique_str.encode('utf-8'))
                key = m.hexdigest()
            value = cache.get(key)
            if value is not None:
                # logger.info('cache_decorator get cache:%s key:%s' % (func.__name__, key))
                if str(value) == '__default_cache_value__':
                    return None
                else:
                    return value
            else:
                logger.info(
                    'cache_decorator set cache:%s key:%s' %
                    (func.__name__, key))
                value = func(*args, **kwargs)
                if value is None:
                    cache.set(key, '__default_cache_value__', expiration)
                else:
                    cache.set(key, value, expiration)
                return value

        return news

    return wrapper


def expire_view_cache(path, servername, serverport, key_prefix=None):
    '''
    刷新视图缓存
    :param path:url路径
    :param servername:host
    :param serverport:端口
    :param key_prefix:前缀
    :return:是否成功
    '''
    from django.http import HttpRequest
    from django.utils.cache import get_cache_key

    request = HttpRequest()
    request.META = {'SERVER_NAME': servername, 'SERVER_PORT': serverport}
    request.path = path

    key = get_cache_key(request, key_prefix=key_prefix, cache=cache)
    if key:
        logger.info('expire_view_cache:get key:{path}'.format(path=path))
        if cache.get(key):
            cache.delete(key)
        return True
    return False


# @cache_decorator()
# def get_current_site():
#     site = Site.objects.get_current()
#     return site




def generate_code() -> str:
    """生成随机数验证码"""
    return ''.join(random.sample(string.digits, 6))


def parse_dict_to_url(dict):
    from urllib.parse import quote
    url = '&'.join(['{}={}'.format(quote(k, safe='/'), quote(v, safe='/'))
                    for k, v in dict.items()])
    return url


def get_blog_setting():
    value = cache.get('blog_setting')
    if value:
        return value
    else:
        from website.models import SiteSetting
        if not SiteSetting.objects.count():
            setting = SiteSetting()
            setting.sitename = '徐祥苗圃'
            setting.site_description = '徐祥苗圃'
            setting.site_seo_description = '徐祥苗圃'
            setting.site_keywords = '苗圃'
            setting.analyticscode = ''
            setting.beiancode = ''
            setting.show_gongan_code = False
            setting.save()
        value = SiteSetting.objects.first()
        logger.info('set cache get_blog_setting')
        cache.set('site_setting', value)
        return value




# def delete_sidebar_cache():
#     from blog.models import LinkShowType
#     keys = ["sidebar" + x for x in LinkShowType.values]
#     for k in keys:
#         logger.info('delete sidebar key:' + k)
#         cache.delete(k)


def delete_view_cache(prefix, keys):
    from django.core.cache.utils import make_template_fragment_key
    key = make_template_fragment_key(prefix, keys)
    cache.delete(key)
