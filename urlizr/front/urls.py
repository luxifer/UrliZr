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

from django.conf.urls import patterns, include, url


urlpatterns = patterns('urlizr.front.views',
    url(r'^$', 'home', name='home'),
    url(r'^translate/(?P<uid>[a-zA-Z0-9]{8})/$', 'show', name='show'),
    url(r'^(?P<uid>[a-zA-Z0-9]{8}$)', 'translate', name='translate'),
    url(r'^robots.txt$', 'robots', name='robots')
)
