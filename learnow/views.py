# >>>1
""" Views.
   :author: Camilo Yate
   :version: 0.1
   : URL: https://media.readthedocs.org/pdf/django/2.0.x/django.pdf
   :Document: https://docs.djangoproject.com/en/2.0/topics/http/shortcuts/"""


from django.http import HttpResponse
from django.shortcuts import render

import datetime


def current_datetiem(request):
    now = datetime.datetime.now()
    html = "<html><body> It is now %s.</body></html>" % now
    return HttpResponse(html)

# >>> 4
def home(request):
    # >>>> 5
    now = datetime.datetime.now()
    context = {'datetime_now': now}
    return render(request, 'home.html', context)
