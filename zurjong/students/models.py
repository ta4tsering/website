from ast import Sub
from email.policy import default

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from zurjong.teachers.models import StudentAgeRange
from zurjong.users.models import Student


class Subjects(models.Model):
    name = models.CharField(max_length=100)

class StudentProfile(models.Model):

    TIME_AM_OR_PM = (
        ("AM", "AM"),
        ("PM", "PM")
    )

    user = models.OneToOneField(Student, on_delete=models.CASCADE)
    age_range = models.ManyToManyField(StudentAgeRange)
    learning_hour_per_week = models.IntegerField()
    want_to_learn = models.ManyToManyField(Subjects)
    lang_barrier = models.BooleanField(default=False)

    # tuition timing
    tuition_start_time = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    tuition_end_time = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    am_or_pm = models.CharField(max_length=2, choices=TIME_AM_OR_PM, default="PM")

    def __str__(self):
        return f"{self.user.username}"

