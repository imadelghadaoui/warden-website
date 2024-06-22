# management/commands/update_attendance.py

from django.core.management.base import BaseCommand
from dashboard.models import Attendance, PresenceRecords, Student
from datetime import date

class Command(BaseCommand):
    help = 'Update attendance records'

    def handle(self, *args, **kwargs):
        students = Student.objects.all()
        presence_records = PresenceRecords.objects.filter(date=date.today())
        
        if not presence_records.exists():
            self.stdout.write(self.style.WARNING('No presence records for today'))
            return
        
        total_students = students.count()
        total_present = presence_records.filter(present=True).count()
        total_absent = total_students - total_present

        attendance, created = Attendance.objects.update_or_create(
            date=date.today(),
            defaults={
                'total_students': total_students,
                'total_present': total_present,
                'total_absent': total_absent,
                'class_name': 'Your Class Name'  # Replace with actual logic if needed
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS('Attendance record created'))
        else:
            self.stdout.write(self.style.SUCCESS('Attendance record updated'))
