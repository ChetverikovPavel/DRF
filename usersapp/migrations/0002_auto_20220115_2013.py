# Generated by Django 2.2.25 on 2022-01-15 20:13

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usersapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="uuid",
            field=models.UUIDField(
                default=uuid.UUID("6f1a9717-f6ac-4f06-a2a5-30b0762d9c30"), primary_key=True, serialize=False
            ),
        ),
    ]
