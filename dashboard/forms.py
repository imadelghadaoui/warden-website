from django import forms
from .models import Student,PresenceRecords,Class

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'image', 'roll_number', 'email', 'date_of_birth', 'address']
class PresenceRecordForm(forms.ModelForm):
    student = forms.ModelChoiceField(queryset=Student.objects.all(), required=False)
    class_name = forms.ModelChoiceField(queryset=Class.objects.all(), required=False)

    class Meta:
        model = PresenceRecords
        fields = ['student', 'date', 'present', 'class_name']

    # dashboard/forms.py



class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name']
