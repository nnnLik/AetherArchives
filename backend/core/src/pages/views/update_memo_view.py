import uuid
from typing import Any

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core.files.base import ContentFile
from django.core.handlers.wsgi import WSGIRequest
from django.views.generic import TemplateView

from src.core.mixins import LoginRequiredMixin
from src.memos.models import UploadedMemo
from src.memos.services.specification import MemoSpecification


class UpdateMemoTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "memo/update_memo_page.html"
    VALIDATION_ERROR_MSG = (
        "Title and body are required. Description should be less",
        "than 250 char and Title should be less than 100 char.",
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        memo_id = self.kwargs.get("memo_id")
        memo = get_object_or_404(
            UploadedMemo,
            id=memo_id,
            user_id=self.request.user.id,
        )
        context["memo"] = memo
        return context

    def post(self, request: WSGIRequest, *args: Any, **kwargs: dict) -> JsonResponse:
        memo_id: int = self.kwargs.get("memo_id")
        memo: UploadedMemo = get_object_or_404(
            UploadedMemo,
            id=memo_id,
            user_id=request.user.id,
        )

        title: str = request.POST.get("title")
        description: str = request.POST.get("description")
        body: str = request.POST.get("body")

        if not MemoSpecification().is_satisfied(
            title=title,
            description=description,
            body=body,
        ):
            return JsonResponse({"error": self.VALIDATION_ERROR_MSG}, status=400)

        file_content = ContentFile(body.encode("utf-8"))

        memo.title = title
        memo.description = description
        memo.uploaded_file = file_content
        memo.file_size = file_content.size
        memo.save()

        return JsonResponse({"message": "Memo updated successfully."})
