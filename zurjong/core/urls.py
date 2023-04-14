from django.urls import path
from django.views.generic import TemplateView

from .views import home_view

app_name = "core"
urlpatterns = [
    path("", home_view, name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    path(
        "contact/", TemplateView.as_view(template_name="pages/contact.html"), name="contact"
    ),
    path(
        "tibetan/", TemplateView.as_view(template_name="pages/tibetan-section.html"), name="tibetan-section"
    ),
    path(
        "terms-and-conditions/", TemplateView.as_view(template_name="pages/terms_and_conditions.html"), name="terms_and_conditions"
    ),
]
