from django.db import models
from django.contrib.auth.models import User

from .ModelChoices import *

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    address_line_one = models.CharField(max_length=150)
    address_line_two = models.CharField(max_length=150, blank=True)
    city = models.PositiveIntegerField()
    state = models.CharField(max_length=2, choices=STATES)
    zip_code = models.CharField(max_length=10, choices=STATES)
    phone_number = models.CharField(max_length=10, choices=STATES)

    gender = models.CharField(max_length=1, choices=GENDER)
    birth_date = models.DateField(null=True)

    account_type = models.CharField(max_length=1, default="N", choices=ACCOUNT_TYPES)
    is_validated = models.BooleanField()
    validated_date = models.DateField(null=True)

    slogan = models.CharField(max_length=150, default="New User")

    last_call = models.DateField(null=True)
    total_calls = models.PositiveIntegerField()
    total_minutes = models.PositiveIntegerField()

    def __str__(self):
          return "%s's user profile" % self.user

'''
I DONT THINK THIS CODE WILL WORK BECAUSE OF DEPENDENCIES

from django.db.models.signals import post_save

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)
'''
