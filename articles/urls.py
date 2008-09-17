from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail

from models import Article, Category
from views import article_detail

article_info = {
    'queryset': Article.objects.all(),
    'template_object_name': 'article',
}

category_info = {
    'queryset': Category.objects.all(),
    'template_object_name': 'category',
}

urlpatterns = patterns('',
    url(r'^$',
        object_list,
        article_info,
        name='article-list'),
    url(r'^category/(?P<slug>[\w-]+)/$',
        object_detail,
        dict(category_info, slug_field='slug'),
        name='category-detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w-]+)/$',
        article_detail,
        name='article-detail'),
)
