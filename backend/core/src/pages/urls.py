from django.urls import path

from src.pages.views import (
    UserPageTemplateView,
    RegisterView,
    AvatarUploadView,
    CreateMemoTemplateView,
)

urlpatterns = [
    path("", UserPageTemplateView.as_view(), name="user_page"),
    path("register/", RegisterView.as_view(), name="register"),
    path("upload-avatar/", AvatarUploadView.as_view(), name="upload_avatar"),
    path("memo/", CreateMemoTemplateView.as_view(), name="create_memo_page"),
]
