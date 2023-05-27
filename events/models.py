from django.db import models
from users.models import User
# Create your models here.

FEST_CHOICES = (
    ('syntaxia','SYNTAXIA'),
    ('multiplexer', 'MULTIPLEXER'),
    ('gaming','GAMING'),
)
class Event(models.Model):
    event_id = models.IntegerField(primary_key=True)
    event_name = models.CharField(max_length=200,null=False,blank=False)
    event_date = models.DateField(null=True,blank=True)
    event_time = models.TimeField(null=True,blank=True)
    event_duration = models.CharField(max_length=200,null=True,blank=True)
    event_location = models.CharField(max_length=200,null=True,blank=True)
    event_description = models.TextField(null=True,blank=True)
    event_attendees = models.IntegerField(default=0,null=False,blank=False)
    event_attendees_limit = models.IntegerField(default=0,null=False,blank=False)
    event_attendees_list = models.TextField(default="",null=True, blank=True)
    event_winners_list = models.TextField(default="",null=True, blank=True)
    users = models.ManyToManyField(User, through='EventRegistration')
    fest = models.CharField(max_length=15, choices=FEST_CHOICES, default=None,null=False,blank=False)
    rules = models.TextField(null=True,blank=True)
    img_url = models.CharField(max_length=200,null=True,blank=True)
    prereq = models.TextField(null=True,blank=True)
    team_limit = models.IntegerField(default=1,null=False,blank=False)
    event_head = models.CharField(max_length=200,null=True,blank=True)
    event_head_contact = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.event_name

class EventRegistration(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_registration_date = models.DateField(null=True,blank=True,auto_now_add=True)
    event_registration_time = models.TimeField(null=True,blank=True,auto_now_add=True)
    class Meta:
        unique_together = (('event_id', 'user'),)
    def __str__(self):
        return self.user.email + " " + self.event_id.event_name