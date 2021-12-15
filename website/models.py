from django.db import models
from django.db.models.fields import TextField
from django.utils.timezone import now
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_time = models.DateTimeField('创建时间', default=now)
    updated_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        abstract = True


class Product(BaseModel):
    """产品"""

    STATUS_CHOICE = (
        ('0', '不发布'),
        ('1', '发布')
    )

    name = models.CharField('产品名称', max_length=36, unique=True)
    intro = models.CharField('产品介绍', max_length=200)
    content = RichTextUploadingField('正文')
    pic = models.ImageField('图片', upload_to='product')
    price = models.IntegerField('价格', default=0)
    order = models.IntegerField('排序,数字越大越靠前', default=0)
    height = models.IntegerField('高度（厘米）', default=100)
    diameter = models.IntegerField('直径（厘米）', default=10)
    status = models.CharField(
        '状态', max_length=1, choices=STATUS_CHOICE, default='1')
    pub_time = models.DateTimeField('发布时间', default=now)
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['-order', 'pub_time']
        verbose_name = '产品'
        verbose_name_plural = verbose_name
        get_latest_by = 'id'


class ProductSpecs(BaseModel):
    """产品规格"""
    STATUS_CHOICE = (
        ('0', '不发布'),
        ('1', '发布')
    )
    name = models.CharField('产品名称', max_length=36, unique=False)
    height = models.IntegerField('高度（厘米）', default=100)
    diameter = models.IntegerField('直径（厘米）', default=10)
    price = models.IntegerField('价格', default=0)
    status = models.CharField(
        '状态', max_length=1, choices=STATUS_CHOICE, default='1')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_specs')

    class Meta:
        verbose_name = '产品规格'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Category(BaseModel):
    """产品类别"""
    STATUS_CHOICE = (
        ('0', '不发布'),
        ('1', '发布')
    )
    name = models.CharField('类别名称', max_length=36, unique=True)

    description = models.CharField('类别介绍', max_length=200)

    status = models.CharField(
        '状态', max_length=1, choices=STATUS_CHOICE, default='1')

    def __str__(self) -> str:
        return self.name

    class Meta:
        # ordering = ['-order', 'pub_time']
        verbose_name = '产品类别'
        verbose_name_plural = verbose_name
        get_latest_by = 'id'


class Banner(BaseModel):
    """Banner图"""

    STATUS_CHOICE = (
        ('0', '不显示'),
        ('1', '显示'),
    )
    name = models.CharField('图片名称', max_length=36, unique=True)

    pic = models.ImageField(verbose_name='图片地址', upload_to='banner')

    intro = models.CharField('图片介绍', max_length=200)

    status = models.CharField(
        '状态', max_length=1, choices=STATUS_CHOICE, default='1')

    def __str__(self) -> str:
        return self.name

    class Meta:
        # ordering = ['-order', 'pub_time']
        verbose_name = 'Banner图'
        verbose_name_plural = verbose_name
        get_latest_by = 'id'


class About(BaseModel):
    """关于"""

    STATUS_CHOICE = (
        ('0', '不生效'),
        ('1', '生效'),
    )
    CATEGORY_CHOICE = (
        ('about', '关于我们'),
        ('concat', '联系我们'),
    )

    name = models.CharField('名称', max_length=10, unique=True)

    category = models.CharField(
        '类别', max_length=36, choices=CATEGORY_CHOICE, default='1')

    pic = models.ImageField(verbose_name='简介图片', upload_to='about')

    content = RichTextUploadingField('正文')

    status = models.CharField('状态', max_length=1, choices=STATUS_CHOICE)

    def __str__(self) -> str:
        return self.name

    class Meta:
        # ordering = ['-order', 'pub_time']
        verbose_name = '相关信息'
        verbose_name_plural = verbose_name
        get_latest_by = 'id'


class Case(BaseModel):
    """案例展示"""

    STATUS_CHOICE = (
        ('0', '草稿'),
        ('1', '发布'),
    )

    title = models.CharField('标题', max_length=10, unique=True)

    pic = models.ImageField(verbose_name='简介图片', upload_to='news')

    content = RichTextUploadingField('正文')

    status = models.CharField('状态', max_length=1, choices=STATUS_CHOICE)

    def __str__(self) -> str:
        return self.title

    class Meta:
        # ordering = ['-order', 'pub_time']
        verbose_name = '案例展示'
        verbose_name_plural = verbose_name
        get_latest_by = 'id'


class News(BaseModel):
    """新闻"""

    STATUS_CHOICE = (
        ('0', '草稿'),
        ('1', '发布'),
    )

    title = models.CharField('标题', max_length=10, unique=True)

    pic = models.ImageField(verbose_name='简介图片', upload_to='news')

    content = RichTextUploadingField('正文')

    status = models.CharField('状态', max_length=1, choices=STATUS_CHOICE)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['-created_time']
        verbose_name = '新闻'
        verbose_name_plural = verbose_name
        get_latest_by = 'id'


class Links(BaseModel):
    """友情链接"""

    name = models.CharField('链接名称', max_length=30, unique=True)
    link = models.URLField('链接地址')
    order = models.IntegerField('排序')
    status = models.BooleanField(
        '是否显示', default=True, blank=False, null=False)

    class Meta:
        ordering = ['order']
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class SiteSetting(models.Model):
    """站点设置"""
    sitename = models.CharField(
        "网站名称",
        max_length=200,
        null=False,
        blank=False,
        default='')
    description = models.TextField(
        "网站描述",
        max_length=1000,
        null=False,
        blank=False,
        default='')
    seo_description = models.TextField(
        "网站SEO描述", max_length=1000, null=False, blank=False, default='')
    keywords = models.TextField(
        "网站关键字",
        max_length=1000,
        null=False,
        blank=False,
        default='')
    beiancode = models.CharField(
        '备案号',
        max_length=2000,
        null=True,
        blank=True,
        default='')
    show_gongan_code = models.BooleanField(
        '是否显示公安备案号', default=False, null=False)
    gongan_beiancode = models.TextField(
        '公安备案号',
        max_length=2000,
        null=True,
        blank=True,
        default='')
    analyticscode = models.TextField(
        "网站统计代码",
        max_length=1000,
        null=False,
        blank=False,
        default='')

    class Meta:
        verbose_name = '站点设置'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sitename
