from django.views.generic import TemplateView

from src.core.mixins import LoginRequiredMixin
from src.memos.models import UploadedMemo


class UserPageTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "user_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["memos"] = UploadedMemo.objects.filter(
            user=self.request.user,
        )
        return context
