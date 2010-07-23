from django.conf.urls.defaults import *

urlpatterns = patterns('piki.views',
    (r'^(?P<page_name>[^/]+)/edit/$', 'edit_page'),
    (r'^(?P<page_name>[^/]+)/save/$', 'save_page'),
    (r'^(?P<page_name>[^/]+)/$', 'view_page'),
)