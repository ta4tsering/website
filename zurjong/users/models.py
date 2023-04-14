from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for Zurjong.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    class Types(models.TextChoices):
        TEACHER = 'T', _('Teacher')
        STUDENT = 'S', _('Student')

    name = CharField(_("Full Name"), blank=True, max_length=255)
    type = models.CharField(max_length=1, choices=Types.choices, default=Types.TEACHER)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

class TeacherManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.TEACHER)

class Teacher(User):
    objects = TeacherManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.TEACHER
        return super().save(*args, **kwargs)

class StudentManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.STUDENT)

class Student(User):
    objects = StudentManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.STUDENT
        return super().save(*args, **kwargs)
