from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import View
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class Home(View):
    def get(self, request):
        params = {}
        return render_to_response('home.html', params)

class About(View):
    def get(self, request):
        params = {}
        return render_to_response('about.html', params)

class Debug(View):
    def get(self, request):
        params = {}
        return render_to_response('debug.html', params)

class Video(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Video, self).dispatch(*args, **kwargs)

    def get(self, request):
        params = {}
        return render_to_response('video.html', params)

class Login(View):
    def get(self, request):
        params = {}
        params.update(csrf(request))
        return render_to_response('login.html', params)

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/choicevrs/video/')
        else:
            return redirect('/accounts/login/')

class Logout(View):
    def get(self, request):
        auth.logout(request)
        params = {}
        return redirect('/', params)

class Register(View):

    def get(self, request):
        params = {}
        params.update(csrf(request))
        params['form'] = UserCreationForm()
        return render_to_response('register.html', params)

    def post(self, request):
        params = {}
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/choicevrs/video/')
        else:
            print 'is not valid!'
            return self.get(request)






'''
this stuff was all old testing.


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
