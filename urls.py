from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'djangows.views.index'),
    (r'^teste$', 'djangows.views.hello_world_service'),
    (r'^teste.wsdl$', 'djangows.views.hello_world_service'),
)
