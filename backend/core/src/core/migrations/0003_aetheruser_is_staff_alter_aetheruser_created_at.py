# Generated by Django 5.0.7 on 2024-08-03 01:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_aetheruser_managers_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="aetheruser",
            name="is_staff",
            field=models.BooleanField(
                default=False,
                help_text="Designates whether the user can log into this admin site.",
                verbose_name="staff status",
            ),
        ),
        migrations.AlterField(
            model_name="aetheruser",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime.now, verbose_name="created_at"
            ),
        ),
    ]