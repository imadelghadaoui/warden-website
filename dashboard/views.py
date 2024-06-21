# dashboard/views.py
from datetime import timezone
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# views.py
from django.shortcuts import get_object_or_404
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, PresenceRecords , Attendance , Class
from .serializers import StudentSerializer, PresenceRecordSerializer
from .forms import StudentForm,PresenceRecordForm , ClassForm, AttendanceForm
from django.shortcuts import render, redirect




#@login_required


def dashboard(request):
    attendance_data = Attendance.objects.all()
    context = {
        'attendance_data': attendance_data,
    }
    return render(request, 'dashboard.html', context)

@api_view(['GET'])
def list_students(request):
    students = Student.objects.all()
    return render(request, 'Students/students.html', {'students': students})

def aggregate_and_update_attendance():
    # Retrieve all classes for which you want to aggregate attendance
    classes = Class.objects.all()

    for class_obj in classes:
        # Filter presence records for the current class
        presence_records = PresenceRecords.objects.filter(class_name=class_obj)

        # Aggregate data
        total_students = presence_records.count()
        total_present = presence_records.filter(present=True).count()
        total_absent = total_students - total_present

        # Get or create attendance record for the class and current date
        attendance_date = timezone.now().date()  # or any date you want to use
        attendance, created = Attendance.objects.get_or_create(
            date=attendance_date,
            class_name=class_obj,
            defaults={
                'total_students': total_students,
                'total_present': total_present,
                'total_absent': total_absent,
            }
        )

        if not created:
            # Update existing attendance record if it already exists
            attendance.total_students = total_students
            attendance.total_present = total_present
            attendance.total_absent = total_absent
            attendance.save()

def aggregate_attendance_view(request):
    # Call the function to aggregate and update attendance
    aggregate_and_update_attendance()

    # Redirect or render as needed
    return redirect('dashboard')  # Replace with your dashboard URL name


def store_new_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data to create a new student
            return redirect('list_students')  # Redirect to a success page
    else:
        form = StudentForm()
    return render(request, 'Students/AddStudent.html', {'form': form})

@api_view(['PUT'])
def api_edit_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'PUT':
        form = StudentForm(request.data, instance=student)
        if form.is_valid():
            form.save()
            return Response({'success': 'Student information has been updated successfully.'})
        return Response(form.errors, status=400)
    return Response({'error': 'Invalid request method'}, status=405)

def edit_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'Students/Edit/EditStudent.html', {'form': form})


@api_view(['DELETE', 'GET', 'POST'])
def delete_student(request, student_id):
    student = get_object_or_404(Student, roll_number=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('list_students')
    return render(request, 'Students/Delete/DeleteStudent.html', {'student': student})



def view_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'Students/View/view_student.html', {'student': student})


# views.py


def presence_create(request):
    student_id = request.GET.get('student_id', None)  # Get student_id from query parameters if available
    class_id = request.GET.get('class_id', None)  # Get class_id from query parameters if available

    if request.method == 'POST':
        form = PresenceRecordForm(request.POST)
        if form.is_valid():
            presence_record = form.save(commit=False)
            # Update student and class information if they were provided in the GET request
            if student_id:
                presence_record.student = get_object_or_404(Student, roll_number=student_id)
            if class_id:
                presence_record.class_name = get_object_or_404(Class, id=class_id)
            presence_record.save()
            return redirect(reverse('get_presence_records', kwargs={'student_id': presence_record.student.roll_number}))
    else:
        form = PresenceRecordForm(initial={'student': student_id, 'class_name': class_id})

    return render(request, 'presence/presenceAdd.html', {'form': form})

@api_view(['GET'])
def get_presence_records(request, student_id):
    presence_records = PresenceRecords.objects.filter(student_id=student_id)
    return render(request, 'presence/presenceList.html', {'presence_records': presence_records, 'student_id': student_id})

def edit_presence_record(request, record_id):
    record = get_object_or_404(PresenceRecords, id=record_id)
    if request.method == 'POST':
        form = PresenceRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('get_presence_records', student_id=record.student.roll_number)
    else:
        form = PresenceRecordForm(instance=record)
    
    return render(request, 'presence/presence_edit.html', {'form': form, 'record': record})

def delete_presence_record(request, record_id):
    record = get_object_or_404(PresenceRecords, id=record_id)
    student_id = record.student.roll_number
    record.delete()
    return redirect('get_presence_records', student_id=student_id)



def add_class(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_list')  # Redirect to a class list view or any other view
    else:
        form = ClassForm()
    return render(request, 'add_class.html', {'form': form})

def class_list(request):
    classes = Class.objects.all()
    print(classes)
    return render(request, 'class_list.html', {'classes': classes})

def delete_class(request, class_id):
    class_to_delete = get_object_or_404(Class, id=class_id)
    class_to_delete.delete()
    return redirect(reverse('class_list'))