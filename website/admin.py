from django.contrib import admin
from .models import Product, Category, Banner, About
# Register your models here.

admin.site.register([Product, Category, Banner, About])