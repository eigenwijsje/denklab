from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from denklab.projects.models import Project, Release, Download, Link, Document

class DownloadInline(admin.TabularInline):
    model = Download
    verbose_name = _('download')
    verbose_name_plural = _('downloads')

class LinkInline(admin.TabularInline):
    model = Link
    verbose_name = _('link')
    verbose_name_plural = _('links')

class ReleaseInline(admin.StackedInline):
    model = Release
    verbose_name = _('release')
    verbose_name_plural = _('releases')

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ReleaseInline]
    list_display = ('name', 'summary')
    prepopulate_from = {'slug': ('name',)}

class ReleaseAdmin(admin.ModelAdmin):
    date_hierarchy = 'released'
    inlines = [DownloadInline, LinkInline]
    list_display = ('version', 'name', 'released')
    list_filter = ('project',)
    prepopulated_fields = {'slug': ('version',)}

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'revision', 'added')
    list_filter = ('project',)
    prepopulated_fields = {'slug': ('title',)}
    save_as = True

admin.site.register(Project, ProjectAdmin)
admin.site.register(Release, ReleaseAdmin)
admin.site.register(Document, DocumentAdmin)
