from django.shortcuts import render_to_response,redirect
from urlizr.front.models import Urliz
from django.http import HttpResponse,Http404
from django.core.exceptions import ValidationError

def translate(request, method, url):
  u = Urliz()
  u.url = url
  try:
    u.full_clean()
  except ValidationError, e:
    data = e.message_dict
    raise Http404 #HttpResponse(data, mimetype='text/plain')

  u.save()

  if method == 'raw':
    return redirect('raw', uid=u.uid)
    
  return render_to_response('api/translate.html', {
    'method': method,
    'url': url,
    })

def raw(request, uid):
  return render_to_response('api/translate.html', {
    'method':'raw',
    'url': uid,
    })
