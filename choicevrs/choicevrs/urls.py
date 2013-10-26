from django.conf.urls import patterns, include

import sys
print sys.path

urlpatterns = patterns('',(r'^', include('choicevrsapp.urls')),)

