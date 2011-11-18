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

from django.shortcuts import render_to_response,redirect
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from UrliZr.front.forms import UrlizForm
from UrliZr.front.models import Urliz
from django.db.models import F

@csrf_protect
def home(request):
  if request.method == 'POST':
    form = UrlizForm(request.POST)
    if form.is_valid():
      if Urliz.objects.filter(url__exact=form.cleaned_data['url']).count() == 0:
        u = Urliz(url=form.cleaned_data['url'])
        u.save()
      else:
        u = Urliz.objects.get(url=form.cleaned_data['url'])
      return redirect('show', uid=u.uid)
    
  else:
    form = UrlizForm()

  return render_to_response('home.html', {
    'form': form,
  }, context_instance=RequestContext(request))

def translate(request, uid):
  u = Urliz.objects.get(uid=uid)
  u.hit = F('hit') + 1
  u.save()
  return render_to_response('redirect.html', {
    'url': u.url,
  })

@csrf_protect
def show(request, uid):
  form = UrlizForm()
  url = Urliz.objects.get(uid=uid)
  host = request.get_host()
  return render_to_response('show.html', {
    'form': form,
    'url': url,
    'host': host,
  }, context_instance=RequestContext(request))
