# Generated by Django 5.0.7 on 2024-08-03 18:48

import src.core.models.aether_user
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_aetheruser_is_staff_alter_aetheruser_created_at"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="aetheruser",
            managers=[
                ("objects", src.core.models.aether_user.AetherUserManager()),
            ],
        ),
    ]
