from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.paginator import Paginator
from .models import Banner, Product, Category, About, News
# Create your views here.

PAGE_SIZE = 12

def index_view(request):
    """首页"""
    # banner_list = Banner.objects.all()
    # return render(request, 'index_next.html', {'banner_list': banner_list})
    # return render(request, 'test.html', {'banner_list': banner_list})
    return render(request, 'index.html')


def product_list(request, category_id, page_num):
    """产品列表"""
    products = Product.objects.filter(status='1', category_id=category_id)
    paginator = Paginator(products, settings.PAGE_SIZE)
    page = paginator.get_page(page_num)
    return render(request, 'test.html', locals())


def product_detail(request, id):
    """产品详情"""
    product = Product.objects.get(pk=id)
    return render(request, 'test.html', locals())
    pass


def about_us(request):
    """关于我们"""
    info = About.objects.filter(category='about').first()
    return render(request, 'test.html', locals())


def concat_us(request):
    """关于我们"""
    info = About.objects.filter(category='concat').first()
    return render(request, 'test.html', locals())


def news_list(request, page_num):
    news = News.objects.all()
    paginator = Paginator(news, settings.PAGE_SIZE)
    page = paginator(page_num)
    return render(request, 'test.html', locals())

def news_detail(request, id):
    news = News.objects.get(pk=id)
    return render(request, 'test.html', locals())

def seed_product(request):
    """插入产品数据"""
    pass
    return HttpResponse('pass seed')
    return
    for i in range(100):
        name = "产品名称-{}".format(i)
        intro = "产品简介-{}".format(i)
        content = "产品内容-{}".format(i)
        pic = 'product/1-200910112TQB.jpg'
        price = 1 * 10
        height = 100
        diameter = 10
        status = '1'
        category = Category.objects.first()
        Product.objects.create(name=name, intro=intro, content=content, price=price,
                               height=height, diameter=diameter, pic=pic, status=status, category=category)
def seed_news(request):
    """插入新闻数据"""
    # pass
    # return HttpResponse('pass seed')
    # return
    for i in range(100):
        title = "新闻标题-{}".format(i)
        content = "新闻内容-{}".format(i)
        pic = 'product/1-200910112TQB.jpg'
        status = '1'
        
        News.objects.create(title=title, content=content, pic=pic, status=status)
