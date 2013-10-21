from django.contrib import admin
from testapp.models import Poll



class PollAdmin(admin.ModelAdmin):
    fields = ['question']


admin.site.register(Poll, PollAdmin)
