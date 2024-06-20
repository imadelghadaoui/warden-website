from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone

class Student(models.Model):
    # Define the attributes for the Student model
    name = models.CharField(max_length=100, help_text="Enter the student's name")
    image = models.ImageField(upload_to='student_images/', null=True, blank=True)
    roll_number = models.CharField(max_length=20, unique=True, help_text="Enter the student's roll number")
    email = models.EmailField(unique=True, help_text="Enter the student's email address")
    date_of_birth = models.DateField(help_text="Enter the student's date of birth")
    address = models.TextField(help_text="Enter the student's address", blank=True, null=True)

    def __str__(self):
        # Return a string representation of the Student object
        return self.name

class PresenceRecord(models.Model):
    # Define the PresenceRecord model to track student presence
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now, help_text="Enter the date of the presence record")
    present = models.BooleanField(default=False, help_text="Whether the student was present or not")

    def __str__(self):
        # Return a string representation of the PresenceRecord object
        return f"{self.student.name} - {self.date} - Present: {self.present}"
    
class Classes(models.Model):
    name=models.CharField(max_length=50)
    nombre=models.IntegerField(default=0)
    #id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

