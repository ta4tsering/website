from django import forms

from .models import TeacherProfile


class TeacherProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = ("contact_number", "bio", "qualification", "languages", "students", "curriculums", "fee_per_hour", )
        widgets = {
            "languages": forms.CheckboxSelectMultiple(),
            "students": forms.CheckboxSelectMultiple(),
            "curriculums": forms.CheckboxSelectMultiple(),
        }
