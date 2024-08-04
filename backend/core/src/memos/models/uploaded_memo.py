from django.db import models

from src.core.models import AetherUser


class UploadedMemo(models.Model):
    user = models.ForeignKey(AetherUser, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    uploaded_file = models.FileField(upload_to="uploads/")

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True, null=True)
    file_name = models.CharField(max_length=255, blank=True, null=True)
    file_size = models.PositiveIntegerField(blank=True, null=True)
    file_type = models.CharField(max_length=50, blank=True, null=True)
    file_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.file_name} ({self.file_size} bytes)"

    class Meta:
        verbose_name = "Uploaded Memo"
        verbose_name_plural = "Uploaded Memos"
        unique_together = (("user", "file_name"),)
