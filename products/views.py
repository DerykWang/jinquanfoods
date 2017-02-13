from django.shortcuts import render
from .models import Category, Product, News
from django.conf import settings
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
# Create your views here.


def index(request):
    catelist = Category.objects.all()
    prolist = Product.objects.all()[:8]
    newslist = News.objects.order_by("-created_at")[:2]
    return render(request, 'index.html', locals())


def base(request):
    site_kw = settings.SITE_KEYWORDS
    site_desc = settings.SITE_DESCRIPTION
    return render(request, 'base.html', locals())


def category(request, cate_id):
    catelist = Category.objects.all()
    cate = Category.objects.get(pk=cate_id)
    prolist = Product.objects.all()
    return render(request, 'category.html', locals())


def product(request):
    catelist = Category.objects.all()
    prolist = Product.objects.all()
    amount = len(prolist)
    paginator = Paginator(prolist, 8)
    # 定义分页器,每页4个对象数据
    page = request.GET.get('page')
    try:
        # pros = paginator.page(page)
        prolist = paginator.page(page)
        # 重新得到prolist对象,该对象包括4个Queryset对象
    except(EmptyPage, InvalidPage, PageNotAnInteger):
        # pros = paginator.page(1)
        prolist = paginator.page(1)
    return render(request, 'product.html', locals())


def detail(request, pro_id):
    catelist = Category.objects.all()
    pro = Product.objects.get(pk=pro_id)
    return render(request, 'detail.html', locals())


# def footer(request):
#     catelist = Category.objects.all()
#     return render(request, 'footer.html', locals())


def aboutus(request):
    catelist = Category.objects.all()
    return render(request, 'aboutus.html', locals())


def contectus(request):
    catelist = Category.objects.all()
    return render(request, 'contectus.html', locals())


# def salement(request):
#     # prolist = Product.objects.order_by('-salements')[:8]
#     return render(request, 'salement.html', locals())


def news(request):
    catelist = Category.objects.all()
    newslist = News.objects.all()
    return render(request, 'news.html', locals())


def certificate(request):
    catelist = Category.objects.all()
    return render(request, 'certificate.html', locals())
