from django import forms
from .models import Student,PresenceRecords

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'image', 'roll_number', 'email', 'date_of_birth', 'address']
class PresenceRecordForm(forms.ModelForm):
    class Meta:
        model = PresenceRecords
        fields = ['student', 'date','present']