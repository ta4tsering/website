from django.urls import path

from .views import tutor_list_view, update_profile

app_name = "teachers"
urlpatterns = [
    path("", view=tutor_list_view, name="list"),
    path("~update/", view=update_profile, name="update_profile"),
]
