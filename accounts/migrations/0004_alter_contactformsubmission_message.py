# Generated by Django 5.0.1 on 2024-06-14 22:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_contactformsubmission_message"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactformsubmission",
            name="message",
            field=models.TextField(),
        ),
    ]