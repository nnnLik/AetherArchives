from typing import Any

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

from config.settings import application_consts


class S3BaseStorage(S3Boto3Storage):
    def url(
        self,
        name: str,
        parameters: dict[str, Any] | None = None,
        expire: int | None = None,
        http_method: str | None = None,
    ) -> str:
        url = super().url(name, parameters, expire, http_method)
        return url.replace(
            application_consts.s3_server.AWS_S3_ENDPOINT_URL,
            application_consts.s3_server.MINIO_ACCESS_URL,
        )


class S3StaticStorage(S3BaseStorage):
    location = settings.STATICFILES_LOCATION


class S3MediaStorage(S3BaseStorage):
    pass
