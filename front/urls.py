from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('UrliZr.front.views',
    url(r'^$', 'home', name='home'),
    url(r'^translate/(?P<uid>[a-zA-Z0-9]{8})/$', 'show', name='show'),
    url(r'^(?P<uid>[a-zA-Z0-9]{8}$)', 'translate', name='translate')
)
