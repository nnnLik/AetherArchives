from typing import Any

from django.views.generic import TemplateView
from django.core.paginator import Paginator

from src.core.mixins import LoginRequiredMixin
from src.memos.models import UploadedMemo


class UserPageTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "user_page/user_page.html"
    OBJ_PER_PAGE = 15

    def get_context_data(self, **kwargs: dict) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        memos = UploadedMemo.objects.filter(user_id=self.request.user.id)
        paginator = Paginator(memos, self.OBJ_PER_PAGE)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context["page_obj"] = page_obj
        return context
