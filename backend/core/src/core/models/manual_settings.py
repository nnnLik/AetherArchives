from django.db import models


class ManualSettings(models.Model):
    name = models.CharField(max_length=150, unique=True)
    value = models.CharField(max_length=350)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def get_value_by_name(name: str) -> str | int | None:
        try:
            obj = ManualSettings.objects.get(name=name)
        except ManualSettings.DoesNotExist:
            return None

        try:
            return int(obj.value)
        except ValueError:
            return str(obj.value)
