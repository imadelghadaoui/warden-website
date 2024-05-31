# serializers.py

from rest_framework import serializers
from .models import Student, PresenceRecord

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll_number', 'email', 'date_of_birth', 'address']

class PresenceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresenceRecord
        fields = ['id', 'student', 'date', 'present']