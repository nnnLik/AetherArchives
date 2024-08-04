from django.urls import path

from src.memos.views.upload_memo_view import UploadMemoView

urlpatterns = [
    path("upload_memo/", UploadMemoView.as_view(), name="upload_memo_view"),
]
