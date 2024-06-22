from django.db import models
from django.utils import timezone
from datetime import date

class Class(models.Model):
    name = models.CharField(max_length=255, unique=True, help_text="Enter the class name")
    
    def __str__(self):
        return self.name

class Student(models.Model):
    roll_number = models.CharField(max_length=20, primary_key=True, help_text="Enter the student's roll number", unique=True)
    name = models.CharField(max_length=100, help_text="Enter the student's name")
    image = models.ImageField(upload_to='student_images/', null=True, blank=True)
    email = models.EmailField(unique=True, help_text="Enter the student's email address")
    date_of_birth = models.DateField(help_text="Enter the student's date of birth")
    address = models.TextField(help_text="Enter the student's address", blank=True, null=True)

    def __str__(self):
        return self.name

class PresenceRecords(models.Model):
    student = models.ForeignKey(Student, to_field='roll_number', on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(default=timezone.now, help_text="Enter the date of the presence record")
    present = models.BooleanField(default=False, help_text="Whether the student was present or not")

    def __str__(self):
        return f"{self.student.roll_number} - {self.date} - Present: {self.present}"

    class Meta:
        db_table = 'dashboard_presencerecord'

class Attendance(models.Model):
    date = models.DateField(default=date.today)
    total_students = models.IntegerField()
    total_present = models.IntegerField()
    total_absent = models.IntegerField()
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} - {self.class_name.name}"
    
    @property
    def attendance_rate(self):
        if self.total_students > 0:
            return (self.total_present / self.total_students) * 100
        return None