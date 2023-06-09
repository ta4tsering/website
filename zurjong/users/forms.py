from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django import forms
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .models import Teacher

User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """

class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """

class TeacherSignupForm(SignupForm):
    """
    Form that will be rendered on a Teacher sign up section/screen.
    """

    def save(self, request):
        user = super().save(request)
        user.type = User.Types.TEACHER
        user.save()
        return user

class TeacherUpdateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["name"]

class StudentSignupForm(SignupForm):
    """
    Form that will be rendered on a Teacher sign up section/screen.
    """

    def save(self, request):
        user = super().save(request)
        user.type = User.Types.STUDENT
        user.save()
        return user
