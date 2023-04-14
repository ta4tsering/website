from django.contrib import admin

from .models import Curriculum, Language, StudentAgeRange, TeacherProfile


@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "contact_number", "fee_per_hour")

@admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "subject")

@admin.register(StudentAgeRange)
class StudentAgeRangeAdmin(admin.ModelAdmin):
    list_display = ("name", "low", "high")

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name",)
