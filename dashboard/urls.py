# dashboard/urls.py
from django.urls import path
from .views import dashboard, list_students, store_new_student, update_student, delete_student, create_presence_record, get_presence_records

urlpatterns = [
    path('', dashboard, name='homepage'),
    # You can add more URLs for additional dashboard functionalities
    path('students/', list_students, name='list_students'),
    path('students/new/', store_new_student, name='store_new_student'),
    path('students/<int:student_id>/update/', update_student, name='update_student'),
    path('students/<int:student_id>/delete/', delete_student, name='delete_student'),
    path('presence/', create_presence_record, name='create_presence_record'),
    path('students/<int:student_id>/presence/', get_presence_records, name='get_presence_records'),
    path('dashboard/students/AddStudent/', store_new_student, name='AddStudent'),
]
