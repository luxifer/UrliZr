"""
This file is part of UrliZr.

UrliZr is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

UrliZr is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with UrliZr.  If not, see <http://www.gnu.org/licenses/>.
"""

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('UrliZr.api.views',
  url(r'^bookmarklet/(?P<location>[a-zA-Z0-9:%\.\+\/\=\?\-]*)$', 'bookmarklet', name='bookmarklet'),
  url(r'^translate/(?P<method>(raw|xml|json))$', 'translate', name='translate'),
  url(r'^raw/(?P<uid>[a-zA-Z0-9]{8})/$', 'raw', name='raw'),
  url(r'^json/(?P<uid>[a-zA-Z0-9]{8})/$', 'json', name='json'),
  url(r'^xml/(?P<uid>[a-zA-Z0-9]{8})/$', 'xml', name='xml'),
)
