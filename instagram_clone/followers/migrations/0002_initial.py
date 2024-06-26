# Generated by Django 4.2.13 on 2024-06-13 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("followers", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="follower",
            name="user_from",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="following",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="follower",
            name="user_to",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="followers",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="follower",
            unique_together={("user_from", "user_to")},
        ),
    ]
