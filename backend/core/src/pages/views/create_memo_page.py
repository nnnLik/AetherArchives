import uuid
from typing import Any

from django.core.files.base import ContentFile
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.views.generic import TemplateView

from src.core.mixins import LoginRequiredMixin
from src.memos.models import UploadedMemo


class CreateMemoTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "memo/create_memo_page.html"

    def post(
        self,
        request: WSGIRequest,
        *args: Any,
        **kwargs: dict,
    ) -> JsonResponse:
        title: str = request.POST.get("title")
        description: str = request.POST.get("description")
        body: str = request.POST.get("body")

        if len(title) > 100:
            return JsonResponse(
                {"error": "Title cannot exceed 100 characters."}, status=400
            )

        if len(description) > 250:
            return JsonResponse(
                {"error": "Description cannot exceed 250 characters."}, status=400
            )

        if not title or not body:
            return JsonResponse({"error": "Title and body are required."}, status=400)

        user = request.user
        uuid_str = str(uuid.uuid4())
        file_name = f"{user.id}_{uuid_str}.md"
        file_content = ContentFile(body.encode("utf-8"), name=file_name)

        uploaded_memo = UploadedMemo(
            user=user,
            title=title,
            description=description,
            uploaded_file=file_content,
            file_name=file_name,
            file_size=file_content.size,
            file_type=file_name.split(".")[-1],
            file_url=f"uploads/{file_name}",
        )
        uploaded_memo.save()

        return JsonResponse({"message": "Memo created successfully."})
