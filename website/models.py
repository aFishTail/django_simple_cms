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

    name = models.CharField('产品名称', max_length=20, unique=True)
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


class Category(BaseModel):
    """产品类别"""
    STATUS_CHOICE = (
        ('0', '不发布'),
        ('1', '发布')
    )
    name = models.CharField('类别名称', max_length=20, unique=True)

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
    name = models.CharField('图片名称', max_length=20, unique=True)

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
        '类别', max_length=20, choices=CATEGORY_CHOICE, default='1')

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
        return self.name

    class Meta:
        # ordering = ['-order', 'pub_time']
        verbose_name = '新闻'
        verbose_name_plural = verbose_name
        get_latest_by = 'id'
