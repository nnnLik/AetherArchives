from django.contrib import admin

from src.memos.models import UploadedMemo


@admin.register(UploadedMemo)
class UploadedMemoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "title",
        "created_at",
        "updated_at",
        "uploaded_file",
        "description",
        "file_name",
        "file_size",
        "file_type",
        "file_url",
    )
    search_fields = (
        "id",
        "user_id",
        "file_name",
        "title",
    )
    list_filter = (
        "created_at",
        "updated_at",
    )
    date_hierarchy = "created_at"
    readonly_fields = (
        "id",
        "created_at",
    )
