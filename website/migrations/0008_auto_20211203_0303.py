# Generated by Django 3.2.9 on 2021-12-03 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20211202_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='category',
            field=models.CharField(choices=[('about', '关于我们'), ('concat', '联系我们')], default='1', max_length=20, verbose_name='类别'),
        ),
        migrations.AlterField(
            model_name='about',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='status',
            field=models.CharField(choices=[('0', '不显示'), ('1', '显示')], default='1', max_length=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('0', '不发布'), ('1', '发布')], default='1', max_length=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='product',
            name='diameter',
            field=models.IntegerField(default=10, verbose_name='直径（厘米）'),
        ),
        migrations.AlterField(
            model_name='product',
            name='height',
            field=models.IntegerField(default=100, verbose_name='高度（厘米）'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('0', '不发布'), ('1', '发布')], default='1', max_length=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
    ]
