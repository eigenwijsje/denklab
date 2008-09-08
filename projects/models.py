from django.db import models
from django.utils.translation import ugettext_lazy as _

from datetime import datetime

class Project(models.Model):
    name = models.CharField(_('name'), max_length=64)
    slug = models.SlugField(_('slug'))
    summary = models.CharField(_('summary'), max_length=128)
    link = models.URLField(_('link'), blank=True)
    blog = models.URLField(_('blog'), blank=True)
    description = models.TextField(_('description'))

    class Meta:
        ordering = ('name',)
        verbose_name = _('project')
        verbose_name_plural = _('projects')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('project-detail', [self.slug])

class Release(models.Model):
    project = models.ForeignKey(Project, related_name='releases', verbose_name=_('project'))
    version = models.CharField(_('version'), max_length=16)
    slug = models.SlugField(_('slug'))
    name = models.CharField(_('name'), max_length=128, blank=True)
    notes = models.TextField(_('notes'))
    released = models.DateField(_('date released'))

    class Meta:
        ordering = ('-released',)
        verbose_name = _('release')
        verbose_name_plural = _('releases')

    def __unicode__(self):
        return '%s v%s' % (self.project, self.version)

    @models.permalink
    def get_absolute_url(self):
        return ('release-detail', None,
            {'project_slug': self.project.slug,
                'release_slug': self.slug})

class Download(models.Model):
    release = models.ForeignKey(Release, related_name='downloads', verbose_name=_('release'))
    download = models.FileField(_('download file'), upload_to='downloads')
    summary = models.CharField(_('summary'), max_length=64)
    added = models.DateTimeField(default=datetime.now, editable=False)

    class Meta:
        ordering = ('download',)
        verbose_name = _('download')
        verbose_name_plural = _('downloads')

    def __unicode__(self):
        return self.download

class Link(models.Model):
    release = models.ForeignKey(Release, related_name='links', verbose_name=_('release'))
    link = models.URLField(_('link'))
    summary = models.CharField(_('summary'), max_length=64)
    added = models.DateTimeField(default=datetime.now, editable=False)

    class Meta:
        ordering = ('link',)

    def __unicode__(self):
        return self.link

class Document(models.Model):
    project = models.ForeignKey(Project, related_name='documents', verbose_name=_('project'))
    title = models.CharField(_('title'), max_length=128)
    slug = models.SlugField(_('slug'))
    revision = models.IntegerField(_('revision'))
    document = models.TextField(_('document'))
    added = models.DateTimeField(default=datetime.now, editable=False)

    class Meta:
        ordering = ('title', '-revision',)

    def __unicode__(self):
        return '%s (r%i)' % (self.title, self.revision)

    @models.permalink
    def get_absolute_url(self):
        return ('document-detail', None,
            {'project_slug': self.project.slug,
                'document_slug': self.slug,
                'revision': self.revision})
