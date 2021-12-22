from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index_view, name='index'),
    # re_path(
    #     r'^products/list/$', product, name='product_list'
    # ),
    path('products/list', product_list, name='product_list'),
    path('products/<int:id>', product_detail, name='product_detail'),
    path('products/specs/<int:id>', product_specs, name='product_specs'),
    path('case', case_index, name='case_index'),
    path('case/<int:id>', case_detail, name='case_detail'),
    path('news/list', news_list, name='news_list'),
    path('news/<int:id>', news_detail, name='news_detail'),
    path('about', about_view, name='about_view'),
    path('message', MessageView.as_view(), name='message'),
    # path('seed_product', seed_product, name='seed-product'),
]
