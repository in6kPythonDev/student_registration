#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.forms import PasswordInput, ModelForm, BooleanField, RegexField
from student_registration.student_form import models
from django.utils.translation import ugettext_lazy as _


class StudentForm(ModelForm):

    class Meta:
        model = models.Student

    agree = BooleanField()

    first_name = RegexField(
        label=_('First name'),
        max_length = 20,
        min_length = 2,
        regex = u'^([А-Яа-яёЁa-zA-Z])+$',
        error_messages = {'invalid': _('Letters only')})

    last_name = RegexField(
        label = _('Last name'),
        max_length = 20,
        min_length = 2,
        regex = u'^([А-Яа-яёЁa-zA-Z])+$',
        error_messages = {'invalid': _('Letters only')})

    phone = RegexField(
        label = _('Phone'),
        max_length = 10,
        min_length = 4,
        regex = r'^[0-9]+$',
        error_messages = {'invalid': _('Numbers only')})

    password = RegexField(
        label = _('Password'),
        widget = PasswordInput,
        max_length = 20,
        min_length = 6,
        regex = r'^[a-zA-Z0-9]+$',
        error_messages = {'invalid': _('Letters and numbers only')})


class AboutInfo(ModelForm):

    class Meta:
        model = models.AboutInfo

