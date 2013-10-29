from django.conf.urls import patterns, url

from views import *

urlpatterns = patterns('',
    url(r'^$|^/$|^index.html$|^/index.html$', Home.as_view(), name='home'),
    url(r'^about/$', About.as_view(), name='about'),
    url(r'^accounts/login/$', Login.as_view(), name='login'),
    url(r'^accounts/logout/$', Logout.as_view(), name='logout'),
    url(r'^accounts/register/$', Register.as_view(), name='register'),
    url(r'^choicevrs/video/$', Video.as_view(), name='register'),

    url(r'^debug/$', Debug.as_view(), name='debug'),
)
