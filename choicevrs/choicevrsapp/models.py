import datetime

from django.db import models
from django.contrib.auth.models import User

from .ModelChoices import *

class UserProfile(models.Model):
    #user ptr and address info (email is included in base User class)
    user = models.OneToOneField(User)
    address_line_one = models.CharField(max_length=150)
    address_line_two = models.CharField(max_length=150, blank=True)
    city = models.PositiveIntegerField()
    state = models.CharField(max_length=2, choices=STATES)
    zip_code = models.CharField(max_length=10, choices=STATES)
    phone_number = models.CharField(max_length=10, choices=STATES)
    gender = models.CharField(max_length=1, choices=GENDER)
    birth_date = models.DateField(null=True)

    #account information
    account_type = models.CharField(max_length=1, default="N", choices=ACCOUNT_TYPES)
    is_validated = models.BooleanField(default=False)
    validated_date = models.DateField(null=True)

    #basic call summary information
    slogan = models.CharField(max_length=150, default="New User")
    last_call = models.DateField(null=True)
    total_calls = models.PositiveIntegerField()
    total_minutes = models.PositiveIntegerField()

    def __str__(self):
        return "%s's user profile" % self.user

class CallRelayEvent(models.Model):
    #base information about the users, translators, and the video.
    call_type = models.CharField(max_length=1, choices=CALL_TYPES)
    base_user = models.ForeignKey(UserProfile)
    user_two = models.ForeignKey(UserProfile, null=True) # optional user stub for 3-way
    translator = models.ForeignKey(UserProfile)
    video_session_info = models.ForeignKey(VideoSession)
    dest_phone_number = models.CharField(max_length=10)

    #flags for state, reviews, special circumstances, etc etc.
    in_progress = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    emergency = models.BooleanField(default=False) # designates the call was relayed to emergency
    reviewed_by_base_user = models.BooleanField(default=False)
    reviewed_by_user_two = models.BooleanField(default=False)
    reviewed_by_translator = models.BooleanField(default=False)
    disconnected = models.BooleanField(default=False)
    recorded = models.BooleanField(default=False)

    #call duration information
    start_time = models.DateTimeField(default=datetime.now())
    stop_time = models.DateTimeField(default=datetime.now())
    duration_minutes = models.PositiveIntegerField(default=0)

class VideoSession(models.Model):
    #call provider and session level information.
    active = models.BooleanField(default=False)
    provider = models.CharField(max_length=10, default='TokBox')
    apikey = models.CharField(max_length=16)
    sessionId = models.CharField(max_length=256)
    token = models.CharField(max_length=1024, unique=True)

    #usage statistics
    first_used = models.DateTimeField(null=True)
    last_used = models.DateTimeField(null=True)
    times_used = models.PositiveIntegerField(default=0)
    error_count = models.PositiveIntegerField(default=0)