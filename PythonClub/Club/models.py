from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Meeting(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    agenda = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'meeting'
        verbose_name_plural = 'meetings'


class MeetingMinutes(models.Model):
    meetingid = models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance = models.ManyToManyField(User)
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'meetingminutes'
        verbose_name_plural = 'meetingminutes'


class Resource(models.Model):
    name = models.CharField(max_length=255)
    resourcetype = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)
    dateentered = models.DateField()
    userid = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'resource'
        verbose_name_plural = 'resources'


class Event(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    userid = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'event'
        verbose_name_plural = 'events'
