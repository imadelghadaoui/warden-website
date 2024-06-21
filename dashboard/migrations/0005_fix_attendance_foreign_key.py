from django.db import migrations, models

def create_default_class(apps, schema_editor):
    Class = apps.get_model('dashboard', 'Class')
    default_class, created = Class.objects.get_or_create(name='Default Class Name')
    return default_class

def update_attendance_class(apps, schema_editor):
    Attendance = apps.get_model('dashboard', 'Attendance')
    Class = apps.get_model('dashboard', 'Class')
    default_class = create_default_class(apps, schema_editor)
    Attendance.objects.filter(class_name__isnull=True).update(class_name=default_class)
    Attendance.objects.filter(class_name__name='Your Class Name').update(class_name=default_class)

class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_class_presencerecords_class_name_and_more'),
    ]

    operations = [
        migrations.RunPython(create_default_class),
        migrations.RunPython(update_attendance_class),
    ]
