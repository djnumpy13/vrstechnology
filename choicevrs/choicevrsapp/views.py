from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import View
from django.contrib.auth.forms import UserCreationForm


class Home(View):

    def get(self, request):
        params = {}
        params.update(csrf(request))

        params['form'] = UserCreationForm()

        return render_to_response('register.html', params)

    def post(self, request):

        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response('home.html', params)





'''
    session = request.session
    session.set_test_cookie()
    print session.test_cookie_worked()

    if not session.get('number'):
        print 'no number'
        session['number'] = 1
    else:
        print 'number' + str(session['number'])
        session['number'] = session['number'] + 1

    if request.user.is_authenticated():
        session['authstr'] = 'baby you are on the inside'
    else:
        session['authstr'] = 'you are a regular user.'

    d = {'name': 'jay schulhof',
         'number': session['number'],
         'type': session['authstr'] }

    t = get_template('home.html')
    html = t.render(Context(d))

    response = HttpResponse(html)
    response.set_cookie("something", "yellow")

    return response

'''
