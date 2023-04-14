from django.db import models
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField

from zurjong.users.models import Teacher, User


class StudentAgeRange(models.Model):
    name = models.CharField(max_length=20)
    low = models.IntegerField()
    high = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.low}-{self.high}) years"


class Curriculum(models.Model):

    class Subjects(models.TextChoices):
        MATH = 'MATH', _('Math')
        SCIENCE = 'SCIENCE', _('Science')
        TIBETAN = 'TIBETAN', _('Tibetan')
        CODING = 'CODING', _('Coding')

    name = models.CharField(max_length=100)
    url = models.URLField()
    subject = models.CharField(max_length=20, choices=Subjects.choices)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class TeacherProfile(models.Model):

    user = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name="profile", primary_key=True)
    contact_number = models.CharField(max_length=13, null=True, blank=True)
    bio = HTMLField(null=True, blank=True)
    qualification = HTMLField(null=True, blank=True)
    languages = models.ManyToManyField(Language, blank=True)
    students = models.ManyToManyField(StudentAgeRange, blank=True)
    curriculums = models.ManyToManyField(Curriculum, blank=True)
    fee_per_hour = models.IntegerField(_("Fee per Hour in $ USD"), default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.user.name}"

@receiver(models.signals.post_save, sender=User)
def create_teacher_profile(sender, instance, created, **kwargs):
    if created and instance.type == User.Types.TEACHER:
        TeacherProfile.objects.create(user=instance)
