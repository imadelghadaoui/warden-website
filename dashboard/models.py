from django.db import models

# Create your models here.
from django.utils import timezone

class Student(models.Model):
    # Define the attributes for the Student model
    roll_number = models.CharField(max_length=20, primary_key=True, help_text="Enter the student's roll number", unique=True)
    name = models.CharField(max_length=100, help_text="Enter the student's name")
    image = models.ImageField(upload_to='student_images/', null=True, blank=True)
    email = models.EmailField(unique=True, help_text="Enter the student's email address")
    date_of_birth = models.DateField(help_text="Enter the student's date of birth")
    address = models.TextField(help_text="Enter the student's address", blank=True, null=True)

    def __str__(self):
        # Return a string representation of the Student object
        return self.name

class PresenceRecords(models.Model):
    # Define the PresenceRecord model to track student presence
    student = models.ForeignKey(Student,to_field='roll_number', on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now, help_text="Enter the date of the presence record")
    present = models.BooleanField(default=False, help_text="Whether the student was present or not")

    def __str__(self):
        # Return a string representation of the PresenceRecord object
        return f"{self.student.roll_number} - {self.date} - Present: {self.present}"
    class Meta:
        db_table = 'dashboard_presencerecord'
class Attendance(models.Model):
    class_name = models.CharField(max_length=100)
    total_students = models.IntegerField(default=0)  # Default value for total students
    total_present = models.IntegerField(default=0)  # Default value for total present
    total_absent = models.IntegerField(default=0)  # Default value for total absent

    def calculate_totals(self):
        # Calculate total students
        self.total_students = Student.objects.count()
        
        # Calculate total present and absent for a specific date (e.g., today's date)
        from django.utils import timezone
        today = timezone.now().date()
        self.total_present = PresenceRecords.objects.filter(date=today, present=True).count()
        self.total_absent = PresenceRecords.objects.filter(date=today, present=False).count()

    def save(self, *args, **kwargs):
        self.calculate_totals()  # Calculate totals before saving
        super().save(*args, **kwargs)  # Call the parent class's save method

    def __str__(self):
        return self.class_name  # Customize the string representation as needed