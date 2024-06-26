# Generated by Django 5.0.6 on 2024-06-21 15:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_attendance_date_alter_attendance_class_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the class name', max_length=255, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='presencerecords',
            name='class_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.class'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='class_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.class'),
        ),
    ]
