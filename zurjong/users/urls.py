from django.urls import path

from zurjong.users.views import (
    student_signup,
    teacher_signup,
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path("signup/teacher/", view=teacher_signup, name="signup_teacher"),
    path("signup/student/", view=student_signup, name="signup_student"),
]
