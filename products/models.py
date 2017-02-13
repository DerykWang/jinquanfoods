# -*-coding:utf8-*-
from django.db import models

# Create your models here


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField('name', max_length=50)
    slug = models.SlugField('slug', max_length=50,
                            help_text='This is slug.', unique=True)
    description = models.TextField('description', max_length=200, blank=True)
    created_at = models.DateTimeField('created_at', auto_now_add=True)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('name', max_length=50)
    price = models.DecimalField('price', max_digits=6, decimal_places=2)
    size = models.CharField('size', max_length=30)
    description = models.TextField('description', max_length=200)
    img = models.ImageField('img')
    created_at = models.DateTimeField('created_at', auto_now_add=True)
    update_at = models.DateTimeField('update_at', auto_now=True)
    salements = models.IntegerField('销量', help_text="数字越大,在主页热销产品中越靠前")
    catelog = models.ManyToManyField(Category)

    class Meta:
        db_table = 'product'
        ordering = ['-salements']

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField('title', max_length=50)
    content = models.TextField('content', max_length=1000)
    img = models.ImageField('img', blank=True)
    created_at = models.DateTimeField('created_at', auto_now_add=True)

    class Meta:
        db_table = 'news'

    def __str__(self):
        return self.title
