from django.db import transaction
from django import forms
from .models import *


class StudentRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=20)
    email = forms.EmailField(label='email')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        # email2 = self.cleaned_data.get('email2')

        # if email != email2:
        #     raise forms.ValidationError('email not match')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('email already exists')

        if not email.endswith('@vvit.net'):
            raise forms.ValidationError('enter valid email')

        return super(StudentRegisterForm, self).clean(*args, **kwargs)


class TeacherRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=20)
    email = forms.EmailField(label='email')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        # email2 = self.cleaned_data.get('email2')

        # if email != email2:
        #     raise forms.ValidationError('email not match')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('email already exists')

        return super(TeacherRegisterForm, self).clean(*args, **kwargs)
    # @transaction.atomic
    # def save(self):
    #     user = super().save(commit=False)
    #     user.is_student = True
    #     user.first_name = self.cleaned_data.get('first_name')
    #     user.last_name = self.cleaned_data.get('last_name')
    #     user.save()
    #     student = Student.objects.create(user=user)
    #     student.username = self.cleaned_data.get('username')
    #     student.save()
    #     return student
