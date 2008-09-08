from django.db import models
from django.utils.translation import ugettext_lazy as _

from datetime import datetime

class Category(models.Model):
    name = models.CharField(_('name'), max_length=32)
    slug = models.SlugField(_('slug'), unique=True)

    class Meta:
        ordering = ('slug',)
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __unicode__(self):
        return self.slug

    @models.permalink
    def get_absolute_url(self):
        return ('category-detail', [self.slug])

class Article(models.Model):
    title = models.CharField(_('title'), max_length=256, unique=True)
    slug = models.SlugField(_('slug'), unique_for_month='published')
    intro = models.TextField(_('intro'))
    body = models.TextField(_('body'))
    published = models.DateTimeField(editable=False, default=datetime.now)
    last_updated = models.DateTimeField(editable=False, blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='articles', verbose_name=_('categories'))

    class Meta:
        ordering = ('-published',)
        get_latest_by = 'published'
        verbose_name = _('article')
        verbose_name_plural = _('articles')

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('article-detail', None,
            {'year': self.published.year,
                'month': self.published.month,
                'slug': self.slug})

    def save(self):
        if self.pk:
            self.last_updated = datetime.now()
        
        super(Article, self).save()
