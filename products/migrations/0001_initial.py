# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-28 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('slug', models.SlugField(help_text='This is slug.', unique=True, verbose_name='slug')),
                ('description', models.TextField(blank=True, max_length=200, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('content', models.TextField(max_length=1000, verbose_name='content')),
                ('img', models.ImageField(blank=True, upload_to='', verbose_name='img')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'db_table': 'news',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='price')),
                ('size', models.CharField(max_length=30, verbose_name='size')),
                ('description', models.TextField(max_length=200, verbose_name='description')),
                ('img', models.ImageField(upload_to='', verbose_name='img')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update_at')),
                ('salements', models.IntegerField(help_text='数字越大,在主页热销产品中越靠前', verbose_name='销量')),
                ('catelog', models.ManyToManyField(to='products.Category')),
            ],
            options={
                'db_table': 'product',
                'ordering': ['salements'],
            },
        ),
    ]
