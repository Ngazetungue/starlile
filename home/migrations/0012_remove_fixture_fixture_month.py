# Generated by Django 5.0.6 on 2024-07-30 12:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0011_fixture_fixture_month"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="fixture",
            name="fixture_month",
        ),
    ]
