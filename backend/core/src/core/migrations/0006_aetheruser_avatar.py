# Generated by Django 5.0.7 on 2024-08-04 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_alter_aetheruser_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="aetheruser",
            name="avatar",
            field=models.ImageField(blank=True, null=True, upload_to="avatars/"),
        ),
    ]
