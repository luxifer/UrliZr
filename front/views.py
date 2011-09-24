from django.shortcuts import render_to_response,redirect
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from UrliZr.front.forms import UrlizForm
from UrliZr.front.models import Urliz

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
  return redirect(u.url)

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
