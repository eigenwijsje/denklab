from django.db import models
from django.utils.translation import ugettext_lazy as _

from datetime import datetime

class Presentation(models.Model):
    title = models.CharField(_('title'), max_length=256)
    subtitle = models.CharField(_('subtitle'), max_length=256, blank=True)
    presented = models.DateField(_('date presented'))
    added = models.DateTimeField(default=datetime.now, editable=False)
    name = models.CharField(_('name'), max_length=64)
    slug = models.SlugField(_('slug'), unique=True)
    notes = models.TextField(_('notes'))

    class Meta:
        ordering = ('-presented',)
        get_latest_by = 'presented'
        verbose_name = _('presentation')
        verbose_name_plural = _('presentations')

    def __unicode__(self):
        return '%s: %s' % (self.name, self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('presentation-detail', [self.slug])
    
class Resource(models.Model):
    resource = models.FileField(_('resource file'), upload_to='resources')
    description = models.CharField(_('description'), max_length=128)
    added = models.DateTimeField(default=datetime.now, editable=False)
    presentation = models.ForeignKey(Presentation, related_name='resources', verbose_name=_('presentation'))

    def __unicode__(self):
        return self.description

    @models.permalink
    def get_absolute_url(self):
        return ('resource-detail', [self.resource])
