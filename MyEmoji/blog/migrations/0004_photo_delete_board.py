# Generated by Django 4.1.6 on 2023-04-06 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0003_remove_board_writer_board_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Photo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField(max_length=40, null=True)),
                (
                    "imgfile",
                    models.ImageField(blank=True, null=True, upload_to="images"),
                ),
                ("content", models.TextField()),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("hit", models.PositiveIntegerField(default=0)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(name="Board",),
    ]
