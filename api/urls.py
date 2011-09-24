from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('urlizr.api.views',
  url(r'^translate/(?P<method>(raw|xml|json))/(?P<url>[a-zA-Z0-9-_\./:%]+)$', 'translate', name='translate'),
  url(r'^raw/(?P<uid>[a-zA-Z0-9]{8})/$', 'raw', name='raw'),
  url(r'^json/(?P<uid>[a-zA-Z0-9]{8})/$', 'json', name='json'),
  url(r'^xml/(?P<uid>[a-zA-Z0-9]{8})/$', 'xml', name='xml'),
)
