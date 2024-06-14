# dashboard/urls.py
from django.urls import path
from .views import dashboard, list_students, store_new_student,view_student, edit_student, delete_student, create_presence_record, get_presence_records
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', dashboard, name='Dashboard'),
    # You can add more URLs for additional dashboard functionalities
    path('students/', list_students, name='list_students'),
    path('students/new/', store_new_student, name='store_new_student'),
    path('students/Edit/<int:student_id>/', edit_student, name='edit_student'),
    path('students/Delete/<int:student_id>/', delete_student, name='delete_student'),
    path('presence/', create_presence_record, name='create_presence_record'),
    path('students/<int:student_id>/presence/', get_presence_records, name='get_presence_records'),
    path('dashboard/students/AddStudent/', store_new_student, name='AddStudent'),
    path('students/<int:student_id>/', view_student, name='view_student'),  # New URL pattern

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
