

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Student(models.Model):
    # YEAR = (
    #     ('1st year', '1st year'),
    #     ('2nd year', '2nd year'),
    #     ('3rd year', '3rd year')
    # )
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    # year = models.CharField(max_length=200, choices=YEAR)
    # first_name = models.CharField(max_length=50, null=True)
    # last_name = models.CharField(max_length=50, null=True)
    # email = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    # BRANCH = (
    #     ('1st year', '1st year'),
    #     ('2nd year', '2nd year'),
    #     ('3rd year', '3rd year')
    # )
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    # branch = models.CharField(max_length=200, choices=BRANCH)

    def __str__(self):
        return self.user.username
