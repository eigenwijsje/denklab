from django.conf.urls.defaults import *

from denklab.presentations.models import Presentation

presentation_info = {
    'queryset': Presentation.objects.all(),
    'template_object_name': 'presentation',
}

urlpatterns = patterns('django.views.generic.list_detail',
    url(r'^$',
        'object_list',
        presentation_info,
        name='presentation-list'),
    url(r'^(?P<slug>[\w-]+)/$',
        'object_detail',
        dict(presentation_info, slug_field='slug'),
        name='presentation-detail'),
)
