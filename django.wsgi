import os
import sys

sys.path.append('/home/luxifer')

os.environ['DJANGO_SETTINGS_MODULE'] = 'UrliZr.local_settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

