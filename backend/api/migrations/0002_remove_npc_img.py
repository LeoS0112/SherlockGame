# Generated by Django 4.2.11 on 2024-03-08 22:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="npc",
            name="img",
        ),
    ]
