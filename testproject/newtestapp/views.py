# Create your views here.

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

def home(request):
    d = {'name': 'jay schulhof'}

    t = get_template('home.html')
    html = t.render(Context(d))

    return HttpResponse(html)