from django.conf.urls import patterns, url

# from django.conf.urls import include

from newtestapp.views import VrsRegister

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testproject.views.home', name='home'),
    # url(r'^testproject/', include('testproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'newtestapp.views.home', name='home'),
    url(r'^accounts/login/$', 'newtestapp.views.login', name='login'),
    url(r'^accounts/register/$', VrsRegister.as_view(), name='register'),
)

