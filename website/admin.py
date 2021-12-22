from django.contrib import admin
from .models import Product, Category, Banner, About, News, Case, ProductSpecs, Links, SiteSetting, Message
from django.contrib import messages
from django.utils.translation import ngettext


admin.site.site_header = '管理后台'  # 设置header
admin.site.site_title = '管理后台'   # 设置title
admin.site.index_title = '管理后台'

# Register your models here.

class ProductSpecsInline(admin.TabularInline):
    model = ProductSpecs


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    @admin.action(description='发布')
    def make_published(self, request, queryset):
        updated = queryset.update(status='1')
        self.message_user(request, '%d 个产品被发布' % updated, messages.SUCCESS)

    @admin.action(description='下架')
    def make_sold_out(self, request, queryset):
        updated = queryset.update(status='0')
        self.message_user(request, '%d 个产品被下架' % updated, messages.SUCCESS)

    search_fields = ['name', 'category__name']
    list_display = ['name', 'intro', 'category', 'status', 'pub_time']
    list_editable = ['intro', 'category', 'status', 'pub_time']
    date_hierarchy = 'pub_time'
    list_per_page = 20
    actions = [make_published, make_sold_out]

    inlines = [
        ProductSpecsInline
    ]
    autocomplete_fields = ['category']


@admin.register(ProductSpecs)
class ProductSpecsAdmin(admin.ModelAdmin):
    list_display = ['product', 'name', 'height', 'diameter', 'price', 'status']
    list_display_links = ['name']
    list_editable = ['height', 'diameter', 'price', 'status']
    search_fields = ['product__name']
    list_filter = ['product__name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    pass


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_editable = ['status']


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    pass


@admin.register(Links)
class CaseAdmin(admin.ModelAdmin):
    pass


@admin.register(SiteSetting)
class CaseAdmin(admin.ModelAdmin):
    pass

@admin.register(Message)
class Message(admin.ModelAdmin):
    pass
