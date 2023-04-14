from typing import Any, Dict

from django.views.generic import TemplateView

from zurjong.users.models import Teacher


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        teacher_samples = Teacher.objects.order_by("?")[:10]
        context["teachers"] = teacher_samples
        return context

home_view = HomeView.as_view()
