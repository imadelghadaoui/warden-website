# dashboard/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard/home.html')

from .models import Student

def student_attendance(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'student.html', context)