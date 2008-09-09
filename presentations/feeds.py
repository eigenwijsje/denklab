# encoding: utf-8
from django.contrib.syndication.feeds import Feed

from denklab.presentations.models import Presentation

class PresentationsFeed(Feed):
    title = u'denkLab | Presentaciones'
    link = '/presentations/'
    description = u'Presentaciones'

    def items(self):
        return Presentation.objects.order_by('-presented')[:5]

    def item_pubdate(self, item):
        return item.presented
