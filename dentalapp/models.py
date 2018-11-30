# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from core.models import User

'''
Patient Data
'''
class Patient(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    id_number = models.CharField(max_length=64)
    address = models.TextField(max_length=256)
    mobile = models.CharField(max_length=8)
    email = models.EmailField(max_length=256, null=True)

    def __unicode__(self):
        return '%s,%s,%s,%s,%s' % (
            self.patient_full_name(), self.id_number,self.address,self.mobile,self.email
        )

    def patient_full_name(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name

class Document(models.Model):
    description = models.TextField(max_length=1024)
    location = models.TextField(max_length=1024)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __unicode__(self):
        return '%s, %s, %s' % (
            self.description, self.location, self.patient
        )
'''---------------------------------------------------------------'''

'''
Visit 
'''
class Visit(models.Model):
    visit_date = models.DateTimeField()
    patient = models.ForeignKey(Patient)
    dentist = models.ForeignKey(User)

    def __unicode__(self):
        return '%s, %s, %s' % (
            self. visit_date, self.patient, self.dentist
        )
'''---------------------------------------------------------------'''

'''
Treatment
'''
class Step(models.Model):
    step_name = models.CharField(max_length=256)
    description = models.TextField(max_length=1024)

class Treatment(models.Model):
    treatment_name = models.CharField(max_length=256)
    description = models.TextField(max_length=1024)
    final_step = models.ForeignKey(Step)

class TreatmentSteps(models.Model):
    treatment = models.ForeignKey(Treatment)
    step = models.ForeignKey(Step)
    step_order = models.IntegerField()

    def __unicode__(self):
        return '%s, %s, %s' % (
            self.treatment, self.step, self.step_order
        )
'''---------------------------------------------------------------'''


'''
Problem
'''
class Tooth(models.Model):
    is_baby_tooth = models.BooleanField(default=False)
    tooth = models.CharField(max_length=32)

    def __unicode__(self):
        return '%s,%s' % (
            self.is_baby_tooth, self.tooth
        )

class ProblemCatalog(models.Model):
    problem_name = models.CharField(max_length=256)

    def __str__(self):
        return self.problem_name

class ProblemDetected(models.Model):
    tooth = models.ForeignKey(Tooth, null=True)
    problem_catalog = models.ForeignKey(ProblemCatalog)
    visit = models.ForeignKey(Visit)
    suggested_treatment = models.ForeignKey(Treatment, null=True, related_name='suggestedtreatment')
    selected_treatement = models.ForeignKey(Treatment, null=True, related_name='selectedtreatment')
'''---------------------------------------------------------------'''

'''
Visit Status
'''
class VisitSteps(models.Model):
    visit = models.ForeignKey(Visit)
    treatment_steps = models.ForeignKey(TreatmentSteps)
    problem_detected = models.ForeignKey(ProblemDetected)
    step_time = models.DateTimeField()
    notes = models.TextField(max_length=512)

class VisitStatus(models.Model):
    status_name = models.CharField(max_length=256)

    def __str__(self):
        return self.status_name

class VisitStatusHistory(models.Model):
    status_time = models.DateTimeField()
    visit_status = models.ForeignKey(VisitStatus)
    visit = models.ForeignKey(Visit)

'''---------------------------------------------------------------'''


'''
Anamnesis
'''
class AnamnesisType(models.Model):
    type = models.CharField(max_length=128)

    def __str__(self):
        return self.type

class AnamnesisCatalog(models.Model):
    catalog_name = models.CharField(max_length=256)
    type = models.ForeignKey(AnamnesisType)

class Anamnesis(models.Model):
    user_anamnesis = models.ForeignKey(User)
    notes = models.TextField(max_length=1024, null=True)

class VisitAnamnesis(models.Model):
    anamnesis = models.ForeignKey(Anamnesis)
    catalog = models.ForeignKey(AnamnesisCatalog)
