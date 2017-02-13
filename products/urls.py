# urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    # url(r'base/$', views.base, name="base"),
    url(r'product/$', views.product, name="product"),
    url(r'category/(?P<cate_id>[0-9]+)/$', views.category, name="category"),
    # url(r'category/(?P<cate_id>[0-9]+)/$', views.category, name="category"),
    url(r'detail/(?P<pro_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'aboutus/', views.aboutus, name="aboutus"),
    url(r'contectus/', views.contectus, name="contectus"),
    # url(r'salement', views.salement, name="salement"),
    url(r'certificate/', views.certificate, name="certificate"),
    url(r'news/', views.news, name="news"),
]
