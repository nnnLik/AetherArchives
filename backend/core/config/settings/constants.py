from pydantic import Field
from pydantic_settings import BaseSettings


class BaseEnvSettings(BaseSettings):
    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"


class ServerSettings(BaseEnvSettings):
    SECRET_KEY: str = Field(default="123waewdqdpk)(UE)(@Y(HDihadiansdo9*UY()Q")
    DEBUG: bool = Field(default=True)
    ALLOWED_HOSTS: list[str] = Field(default=["*"])
    CORS_ALLOWED_ORIGINS: list[str] = Field(default=["http://0.0.0.0:3000"])
    CORS_ALLOW_CREDENTIALS: bool = Field(default=True)
    CORS_ALLOW_ALL_ORIGINS: bool = True if DEBUG else False


class DatabaseSettings(BaseEnvSettings):
    ENGINE: str = Field(default="django.db.backends.postgresql")
    DB_NAME: str = Field(default="aetherarchives")
    DB_USER: str = Field(default="aetherarchives")
    DB_PASSWORD: str = Field(default="aetherarchives")
    DB_HOST: str = Field(default="aetherarchives-core-database")
    DB_PORT: int = Field(default=5432)


class HashMapperServiceSettings(BaseEnvSettings):
    SERVICE_URL: str = Field(default="http://test:2228")


class S3ServerSettings(BaseEnvSettings):
    AWS_S3_USER: str = Field(default="aetherarchives")
    AWS_S3_PASSWORD: str = Field(default="aetherarchives")
    AWS_S3_STORAGE_BUCKET_NAME: str = Field(default="aetherarchives")
    AWS_S3_ACCESS_KEY_ID: str = Field(default="...")
    AWS_S3_SECRET_ACCESS_KEY: str = Field(default="...")
    AWS_S3_ENDPOINT_URL: str = Field(default="http://aetherarchives-minio:9999")
    MINIO_ACCESS_URL: str = Field(default="")
    AWS_S3_USE_SSL: bool = Field(default=False)


class ApplicationConsts:
    server: ServerSettings = ServerSettings()
    database: DatabaseSettings = DatabaseSettings()
    hasher_mapper_api: HashMapperServiceSettings = HashMapperServiceSettings()
    s3_server: S3ServerSettings = S3ServerSettings()


application_consts: ApplicationConsts = ApplicationConsts()
