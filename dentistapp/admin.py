# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'patient_number', 'gender', 'location', 'mobile', 'date_registered')

admin.site.register(models.Location)
admin.site.register(models.Patient, PatientAdmin)
admin.site.register(models.PatientAppointment)
admin.site.register(models.AppointmentSchedule)
