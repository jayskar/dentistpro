# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from dentalapp import models

# Customized Admin
class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_full_name', 'id_number', 'mobile', 'email')

# Register your models here.
admin.site.register(models.AnamnesisCatalog)
admin.site.register(models.Anamnesis)
admin.site.register(models.AnamnesisType)
admin.site.register(models.ProblemDetected)
admin.site.register(models.Treatment)
admin.site.register(models.Visit)
admin.site.register(models.ProblemCatalog)
admin.site.register(models.Tooth)
admin.site.register(models.TreatmentSteps)
admin.site.register(models.Patient, PatientAdmin)
admin.site.register(models.Document)
admin.site.register(models.Step)
admin.site.register(models.VisitAnamnesis)
admin.site.register(models.VisitStatusHistory)
admin.site.register(models.VisitSteps)
