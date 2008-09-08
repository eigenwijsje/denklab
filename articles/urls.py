from django.conf.urls.defaults import *

from denklab.articles.models import Article, Category

article_info = {
    'queryset': Article.objects.all(),
    'template_object_name': 'article',
}

category_info = {
    'queryset': Category.objects.all(),
    'template_object_name': 'category',
}

urlpatterns = patterns('django.views.generic.list_detail',
    url(r'^$',
        'object_list',
        article_info,
        name='article-list'),
    url(r'^category/(?P<slug>[\w-]+)/$',
        'object_detail',
        category_info,
        name='category-detail'),
)

urlpatterns += patterns('denklab.articles.views',
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w-]+)/$',
        'article_detail',
        name='article-detail'),
)
