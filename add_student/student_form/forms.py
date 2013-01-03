from django.forms import PasswordInput, ModelForm, BooleanField, RegexField
from add_student.student_form import models


class StudentForm(ModelForm):

    class Meta:
        model = models.Student

    agree = BooleanField()

    first_name = RegexField(
        label='First name',
        max_length = 20,
        min_length = 2,
        regex = r'^[a-zA-Z]+$',
        error_messages = {'invalid': 'Letters only'})

    last_name = RegexField(
        label = 'Last name',
        max_length = 20,
        min_length = 2,
        regex = r'^[a-zA-Z]+$',
        error_messages = {'invalid': 'Letters only'})

    phone = RegexField(
        label = 'Phone',
        max_length = 10,
        min_length = 4,
        regex = r'^[0-9]+$',
        error_messages = {'invalid': 'Numbers only'})

    password = RegexField(
        label = 'Password',
        widget = PasswordInput,
        max_length = 20,
        min_length = 6,
        regex = r'^[a-zA-Z0-9]+$',
        error_messages = {'invalid': 'Letters and numbers only'})