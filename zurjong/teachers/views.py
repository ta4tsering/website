from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import ListView

from zurjong.users.forms import TeacherUpdateForm
from zurjong.users.models import Teacher

from .forms import TeacherProfileUpdateForm


@login_required
def update_profile(request):
    if request.method == "POST":
        teacher_form = TeacherUpdateForm(request.POST, instance=request.user)
        teacher_profile_form = TeacherProfileUpdateForm(request.POST, instance=request.user.profile)

        if teacher_form.is_valid() and teacher_profile_form.is_valid():
            teacher_form.save()
            teacher_profile_form.save()
            messages.success(request, "Your profile was successfully updated!")
            return redirect("users:detail", request.user.username)
    else:
        teacher_form = TeacherUpdateForm(instance=request.user)
        teacher_profile_form = TeacherProfileUpdateForm(instance=request.user.profile)

    context = {
        "teacher_form": teacher_form,
        "teacher_profile_form": teacher_profile_form,
    }

    return render(request, "teachers/profile_update.html", context)


class TutorListView(ListView):
    models = Teacher
    queryset = Teacher.objects.all()
    template_name = "teachers/tutors.html"
    context_object_name = "teachers"

tutor_list_view = TutorListView.as_view()

