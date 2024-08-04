from typing import Any

from rest_framework.generics import CreateAPIView
from rest_framework import serializers, permissions

from src.memos.models import UploadedMemo


class UploadedMemoSerializer(serializers.ModelSerializer):
    uploaded_file = serializers.FileField(allow_empty_file=False)

    class Meta:
        model = UploadedMemo
        fields = (
            "id",
            "user",
            "created_at",
            "updated_at",
            "uploaded_file",
            "description",
            "file_name",
            "file_size",
            "file_type",
            "file_url",
        )
        read_only_fields = (
            "id",
            "user",
            "created_at",
            "updated_at",
            "file_name",
            "file_size",
            "file_type",
            "file_url",
        )

    def create(
        self,
        validated_data: dict[str, Any],
    ) -> UploadedMemo:
        file = validated_data.get("uploaded_file")
        validated_data["file_name"] = file.name
        validated_data["file_size"] = file.size
        validated_data["file_type"] = file.content_type
        validated_data["file_url"] = file.url if hasattr(file, "url") else None
        return super().create(validated_data)


class UploadMemoView(CreateAPIView):
    queryset = UploadedMemo.objects.all()
    serializer_class = UploadedMemoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(
        self,
        serializer: UploadedMemoSerializer,
    ) -> None:
        serializer.save(user=self.request.user)
