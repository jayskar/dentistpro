# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
import uuid
from simple_history.models import HistoricalRecords

_today = datetime.today()

class Location(models.Model):
    PROVINCE_CHOICES = (
        (0, 'Autonomous Region of Bougainville'),
        (1, 'Central'),
        (2, 'Chimbu'),
        (3, 'East New Britain'),
        (4, 'East Sepik)'),
        (5, 'Eastern Highlands'),
        (6, 'Enga'),
        (7, 'Gulf'),
        (8, 'Hela'),
        (9, 'Jiwaka'),
        (10, 'Madang'),
        (11, 'Manus'),
        (12, 'Milne Bay'),
        (13, 'Morobe'),
        (14, 'National Capital District'),
        (15, 'New Ireland'),
        (16, 'Oro (Northern)'),
        (17, 'Sandaun(West Sepik)'),
        (18, 'Southern Highlands'),
        (19, 'West New Britain'),
        (20, 'Western(Fly)'),
        (21, 'Western Highlands')
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    province = models.SmallIntegerField(choices=PROVINCE_CHOICES, default=14)

    ## Simple History
    history = HistoricalRecords()

    def __str__(self):
        return self.name

def generate_number():
    print(_today)
    print(type(_today))
    _yy = _today.strftime('%y')
    random_number = str(uuid.uuid4().int)[:4]
    new_number = _yy + random_number
    return new_number

def generate_unique_number(model_instance):
    p_number = '181013' #generate_number()
    ModelClass = model_instance.__class__
    
    while ModelClass._default_manager.filter(
        **{'patient_number' : p_number}
    ).exists():
        print('number exists, generating a new one')
        p_number = generate_number()

    return p_number


class Patient(models.Model):
    GENDER_CHOICES = (
        (0, '------'),
        (1, 'male'),
        (2, 'female'),
    )
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0)
    location = models.ForeignKey(Location, null=True, blank=True)
    mobile = models.CharField(max_length=8, null=True, blank=True)
    email = models.CharField(max_length=150, null=True, blank=True)
    patient_number = models.CharField(max_length=6, unique=True, verbose_name="Patient Number", editable=False)
    date_of_birth = models.DateField(auto_now=False)
    date_registered = models.DateTimeField(auto_now_add=True)

    ## Simple History
    history = HistoricalRecords()


    def full_name(self):
        '''
        Returns the fist_name plus the last_name, with a space in between
        :return:
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def save(self, *args, **kwargs):
        if not self.patient_number:
            self.patient_number = generate_unique_number(self)
        super(Patient, self).save(*args, **kwargs)

    def __str__(self):
        return '%s [%s]' % (self.full_name(), self.patient_number)

class PatientAppointment(models.Model):
    PATIENT_STATUS_CHOICE = (
        (0, '------'),
        (1, 'new'),
        (3, 'review'),
    )
    patient = models.ForeignKey(Patient, blank=True)
    status = models.SmallIntegerField(choices=PATIENT_STATUS_CHOICE, default=0)
    comments = models.TextField(blank=True)

    ## Simple History
    history = HistoricalRecords()

    def __unicode__(self):
        return '%s, %s' % (self.patient, self.get_status_display())

class AppointmentSchedule(models.Model):
    appointment = models.ForeignKey(PatientAppointment, blank=True, null=True)
    date_visit = models.DateTimeField(auto_now_add=True)

    ## Simple History
    history = HistoricalRecords()

    def __unicode__(self):
        return '%s, %s' % (self.appointment, self.date_visit)