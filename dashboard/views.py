# dashboard/views.py
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# views.py
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, PresenceRecord
from .serializers import StudentSerializer, PresenceRecordSerializer
from .forms import StudentForm
from django.shortcuts import render, redirect



@login_required
def dashboard(request):
    return render(request, 'homepage.html')


@api_view(['GET'])
def list_students(request):
    students = Student.objects.all()
    return render(request, 'Students/students.html', {'students': students})


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
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('list_students')
    return render(request, 'Students/Delete/DeleteStudent.html', {'student': student})



def view_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'Students/View/view_student.html', {'student': student})


@api_view(['POST'])
def create_presence_record(request):
    serializer = PresenceRecordSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_presence_records(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    presence_records = PresenceRecord.objects.filter(student=student)
    serializer = PresenceRecordSerializer(presence_records, many=True)
    return Response(serializer.data)


def attendance_summary(request):
    # Get total number of presence records
    total_records = PresenceRecord.objects.count()

    # Get number of presence records (present=True)
    total_presence = PresenceRecord.objects.filter(present=True).count()

    # Calculate number of absences
    total_absences = total_records - total_presence

    # Calculate attendance rate
    attendance_rate = (total_presence / total_records) * 100 if total_records > 0 else 0
    print(total_presence,total_absences,attendance_rate)
    # Return data as JSON response
    data = {
        'total_presence': total_presence,
        'total_absences': total_absences,
        'attendance_rate': attendance_rate
    }
    return JsonResponse(data)