from django.urls import path

from src.pages.views import (
    UserPageTemplateView,
    RegisterView,
    AvatarUploadView,
    CreateMemoTemplateView,
    UpdateMemoTemplateView,
)

urlpatterns = [
    path("", UserPageTemplateView.as_view(), name="user_page"),
    path("register/", RegisterView.as_view(), name="register"),
    path("upload_avatar/", AvatarUploadView.as_view(), name="upload_avatar"),
    path("create_memo/", CreateMemoTemplateView.as_view(), name="create_memo_page"),
    path(
        "update_memo/<int:memo_id>/",
        UpdateMemoTemplateView.as_view(),
        name="update_memo_page",
    ),
]
