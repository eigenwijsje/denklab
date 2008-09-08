from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

from denklab.articles.feeds import ArticlesFeed, CategoryFeed
from denklab.presentations.feeds import PresentationsFeed

admin.autodiscover()

feeds = (
    {'category': CategoryFeed },
    {'articles': ArticlesFeed,
        'presentations': PresentationsFeed}
)

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^articles/', include('denklab.articles.urls')),
    (r'^presentations/', include('denklab.presentations.urls')),
    (r'^projects/', include('denklab.projects.urls')),
    (r'^contact/', include('contact_form.urls')),
)

urlpatterns += patterns('django.contrib.syndication.views',
    (r'^feeds/articles/(?P<url>.*)/$', 'feed', {'feed_dict': feeds[0]}),
    (r'^feeds/(?P<url>.*)/$', 'feed', {'feed_dict': feeds[1]}),
)
