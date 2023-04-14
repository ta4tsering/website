from typing import Any, List, Optional

from allauth.account.views import SignupView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView

from .forms import StudentSignupForm, TeacherSignupForm

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_template_names(self) -> List[str]:
        if self.request.user.type == User.Types.TEACHER:
            return "teachers/profile.html"
        elif self.request.user.type == User.Types.STUDENT:
            return "students/profile.html"
        else:
            super().get_template_names()

    def get_context_object_name(self, obj: Any) -> Optional[str]:
        if self.request.user.type == User.Types.TEACHER:
            return "teacher"
        elif self.request.user.type == User.Types.STUDENT:
            return "student"
        else:
            super().get_context_object_name(obj)



user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        if self.request.user.type == User.Types.TEACHER:
            if not self.request.user.profile.bio:
                return reverse("teachers:update_profile")
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


class TeacherSignupView(SignupView):
    form_class = TeacherSignupForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_type"] = "Teacher"
        return context

teacher_signup = TeacherSignupView.as_view()

class StudentSignupView(SignupView):
    form_class = StudentSignupForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_type"] = "Student"
        return context

student_signup = StudentSignupView.as_view()
