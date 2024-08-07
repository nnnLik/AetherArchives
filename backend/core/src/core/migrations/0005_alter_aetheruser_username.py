# Generated by Django 5.0.7 on 2024-08-04 06:42

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_alter_aetheruser_managers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aetheruser",
            name="username",
            field=models.CharField(
                error_messages={"unique": "A user with that username already exists."},
                max_length=150,
                validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                verbose_name="username",
            ),
        ),
    ]
