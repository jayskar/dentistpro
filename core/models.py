# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        (1, '---------'),
        (2, 'admin'),
        (3, 'dentist'),
        (4, 'clerk'),
        (5, 'assistant')
    )
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=50, blank=True)
    last_name = models.CharField(_('last name'), max_length=50, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('active'), default=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =  []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the fist_name plus the last_name, with a space in between
        :return:
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user
        :return:
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User
        :return:
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
