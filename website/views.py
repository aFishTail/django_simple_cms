from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.paginator import Paginator
from .models import Banner, Product, Category, About, Case, News

# Create your views here.

PAGE_SIZE = 12


def index_view(request):
    """首页"""
    banner_list = Banner.objects.all()
    product_list = Product.objects.all()[:4]
    case_list = Case.objects.all()[:1]
    news_list = News.objects.all()[:1]
    about = About.objects.filter(status='1').first()
    # return render(request, 'index_next.html', {'banner_list': banner_list})
    # return render(request, 'test.html', {'banner_list': banner_list})
    return render(request, 'index.html', locals())


def product_list(request):
    """产品列表"""
    category_id = request.GET.get('category_id', None)
    page_num = request.GET.get('p', 1)
    if category_id:
        category_id = int(category_id)
        products = Product.objects.filter(status='1', category_id=category_id)
        category_name = Category.objects.get(pk=category_id).name
    else:
        products = Product.objects.filter(status='1')
    categories = Category.objects.filter(status='1')
    paginator = Paginator(products, settings.PAGE_SIZE)
    page = paginator.get_page(page_num)
    return render(request, 'product.html', locals())


def product_detail(request, id):
    """产品详情"""
    product = Product.objects.get(pk=id)
    categories = Category.objects.filter(status='1')
    return render(request, 'product_detail.html', locals())

def product_specs(request, id):
    """产品明细"""
    product = Product.objects.get(pk=id)
    categories = Category.objects.filter(status='1')
    table_data = product.product_specs.all()
    return render(request, 'product_specs.html', locals())



def about_view(request):
    """关于我们"""
    category = request.GET.get('category', 'about')
    info = About.objects.filter(category=category).first()
    return render(request, 'about.html', locals())



def case_index(request):
    case_list = Case.objects.all()
    return render(request, 'case.html', locals())

def case_detail(request, id):
    case = Case.objects.get(pk=id)
    return render(request, 'case_detail.html', locals())


def news_list(request):

    page_num = request.GET.get('p', 1)
    news = News.objects.filter(status='1')
    paginator = Paginator(news, settings.PAGE_SIZE)
    page = paginator.get_page(page_num)
    return render(request, 'news.html', locals())

def news_detail(request, id):
    news = News.objects.get(pk=id)
    return render(request, 'news_detail.html', locals())


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
