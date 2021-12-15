# Generated by Django 3.2.9 on 2021-12-15 06:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_alter_news_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSpecs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('height', models.IntegerField(default=100, verbose_name='高度（厘米）')),
                ('diameter', models.IntegerField(default=10, verbose_name='直径（厘米）')),
                ('price', models.IntegerField(default=0, verbose_name='价格')),
                ('status', models.CharField(choices=[('0', '不发布'), ('1', '发布')], default='1', max_length=1, verbose_name='状态')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.product')),
            ],
            options={
                'verbose_name': '产品规格',
                'verbose_name_plural': '产品规格',
            },
        ),
    ]
