# Create your views here.

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

def home(request):
    session = request.session

    if not session.get('number'):
        print 'no number'
        session['number'] = 1
    else:
        print 'number' + str(session['number'])
        session['number'] = session['number'] + 1

    d = {'name': 'jay schulhof',
         'number': session['number'] }

    t = get_template('home.html')
    html = t.render(Context(d))

    response = HttpResponse(html)
    response.set_cookie("something", "yellow")

    return response
