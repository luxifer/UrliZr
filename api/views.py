from django.shortcuts import render_to_response,redirect
from UrliZr.front.models import Urliz
from UrliZr.front.forms import UrlizForm
from django.http import HttpResponseBadRequest

def translate(request, method, url):
  form = UrlizForm({'url': url})
  
  if form.is_valid():
    if Urliz.objects.filter(url__exact=form.cleaned_data['url']).count() == 0:
      u = Urliz(url=form.cleaned_data['url'])
      u.save()
    else:
      u = Urliz.objects.get(url=form.cleaned_data['url'])

    if method == 'raw':
      return redirect('raw', uid=u.uid)

    elif method == 'json':
      return redirect('json', uid=u.uid)

    elif method == 'xml':
      return redirect('xml', uid=u.uid)

    else:    
      return HttpResponseBadRequest('Invalid request/method')

  else:
    return HttpResponseBadRequest('Invalid URL')

def raw(request, uid):
  return render_to_response('api/raw.tpl', {
    'url': uid,
    'host': request.get_host()
  }, mimetype='text/plain')

def json(request, uid):
  return render_to_response('api/json.tpl', {
    'url': uid,
    'host': request.get_host()
  }, mimetype='text/json')

def xml(request, uid):
  return render_to_response('api/xml.tpl', {
    'url': uid,
    'host': request.get_host()
  }, mimetype='text/xml')
