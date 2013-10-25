# Create your views here.

from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import View



def home(request):

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

    print response
    return response


def login(request):
    state = "Please log in below..."
    username = '' 
    password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('login.html' , {'state':state, 'username': username} )


class VrsRegister(View):

    template = 'register.html'

    def get(self, request):
        params = {}
        params.update(csrf(request))
        return render_to_response(self.template, params)

    def post(self, request):
        params = {}
        params.update(csrf(request))

        username = request.POST.get('username')
        password = request.POST.get('password')
        passwordverification = request.POST.get('passwordverification')
        email = request.POST.get('email')
        emailverification = request.POST.get('emailverification')

        print username
        print password
        print passwordverification
        print email
        print emailverification

        return render_to_response(self.template, params)