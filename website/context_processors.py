import logging
from datetime import datetime

from django_mp.utils import cache, get_blog_setting

logger = logging.getLogger(__name__)


def seo_processor(requests):
    key = 'seo_processor'
    value = cache.get(key)
    if value:
        return value
    else:
        logger.info('set processor cache.')
        setting = get_blog_setting()
        value = {
            'SITE_NAME': setting.sitename,
            'SITE_SEO_DESCRIPTION': setting.seo_description,
            'SITE_DESCRIPTION': setting.description,
            'SITE_KEYWORDS': setting.keywords,
            'BEIAN_CODE': setting.beiancode,
            'ANALYTICS_CODE': setting.analyticscode,
            "BEIAN_CODE_GONGAN": setting.gongan_beiancode,
            "SHOW_GONGAN_CODE": setting.show_gongan_code,
            "CURRENT_YEAR": datetime.now().year}
        cache.set(key, value, 60 * 60 * 10)
        return value
