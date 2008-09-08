from django.conf.urls.defaults import *

from denklab.projects.models import Project

project_info = {
    'queryset': Project.objects.all(),
    'template_object_name': 'project',
}

urlpatterns = patterns('django.views.generic.list_detail',
    url(r'^$',
        'object_list',
        project_info,
        name='project-list'),
    url(r'^(?P<slug>[\w-]+)/$',
        'object_detail',
        dict(project_info, slug_field='slug'),
        name='project-detail'),
)

urlpatterns += patterns('denklab.projects.views',
    url(r'^(?P<project_slug>[\w-]+)/r/$',
        'release_list',
        name='release-list'),
    url(r'^(?P<project_slug>[\w-]+)/r/(?P<release_slug>[\w-]+)/$',
        'release_detail',
        name='release-detail'),
    url(r'^(?P<project_slug>[\w-]+)/d/$',
        'document_list',
        name='document-list'),
    url(r'^(?P<project_slug>[\w-]+)/d/(?P<document_slug>[\w-]+)/(?P<revision>[\d]+)/$',
        'document_detail',
        name='document-detail'),
)
