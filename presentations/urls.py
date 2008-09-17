from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail

from models import Presentation

presentation_info = {
    'queryset': Presentation.objects.all(),
    'template_object_name': 'presentation',
}

urlpatterns = patterns('',
    url(r'^$',
        object_list,
        presentation_info,
        name='presentation-list'),
    url(r'^(?P<slug>[\w-]+)/$',
        object_detail,
        dict(presentation_info, slug_field='slug'),
        name='presentation-detail'),
)
