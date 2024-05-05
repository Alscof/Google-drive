# Generated by Django 5.0.3 on 2024-05-04 18:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("googledriveapp", "0005_remove_file_page_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="folder",
            name="parent_folder",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subfolders",
                to="googledriveapp.folder",
            ),
        ),
    ]