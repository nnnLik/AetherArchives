from django.contrib import admin

from src.core.models import AetherUser


@admin.register(AetherUser)
class AetherUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "is_active",
        "bio",
        "created_at",
        "last_login",
        "password",
        "is_staff",
    )
    search_fields = (
        "id",
        "username",
        "email",
    )
    date_hierarchy = "created_at"
    readonly_fields = (
        "id",
        "created_at",
        "password",
    )
