# encoding: utf-8
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.syndication.feeds import Feed, FeedDoesNotExist

from denklab.articles.models import Article, Category

class ArticlesFeed(Feed):
    title = u'denkLab | Artículos'
    link = '/articles/'
    description = u'Artículos'

    def items(self):
        return Article.objects.order_by('-published')[:5]

    def item_pubdate(self, item):
        return item.published

class CategoryFeed(Feed):
    def get_object(self, bits):
        if len(bits) != 1:
            raise ObjectDoesNotExist

        return Category.objects.get(slug=bits[0])

    def title(self, obj):
        return u'denklab | Artículos en la categoría »%s«' % obj.name

    def link(self, obj):
        if not obj:
            raise FeedDoesNotExist

        return obj.get_absolute_url()

    def description(self, obj):
        return u'Artículos en la categoría »%s«' % obj.name

    def items(self, obj):
        return Article.objects.filter(categories__id=obj.id).order_by('-published')[:5]
    
    def item_pubdate(self, item):
        return item.published
