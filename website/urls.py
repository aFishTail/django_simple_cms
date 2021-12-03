from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index_view, name='index'),
    # re_path(
    #     r'^products/list/$', product, name='product_list'
    # ),
    path(
        'products/list/<int:category_id>/<int:page_num>/', product_list, name='product_list'
    ),
    path(
        'seed_product', seed_product, name='seed-product'
    ),
]
