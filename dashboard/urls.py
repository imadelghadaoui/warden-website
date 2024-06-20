# dashboard/urls.py
from django.urls import path
from .views import dashboard,get_presence_records, list_students, store_new_student,view_student, edit_student, delete_student, presence_create,  get_presence_records,delete_presence_record,edit_presence_record
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', dashboard, name='homepage'),
    # You can add more URLs for additional dashboard functionalities
    path('students/', list_students, name='list_students'),
    path('students/new/', store_new_student, name='store_new_student'),
    path('students/Edit/<int:student_id>/', edit_student, name='edit_student'),
    path('students/Delete/<int:student_id>/', delete_student, name='delete_student'),
    path('students/<int:student_id>/presence/', get_presence_records, name='get_presence_records'),
    path('dashboard/students/AddStudent/', store_new_student, name='AddStudent'),
    path('students/<int:student_id>/', view_student, name='view_student'),  # New URL pattern
    path('presence/', presence_create, name='presence_create'),
   # path('presence/<int:pk>/', manage_presence_record, name='manage_presence_record'),
    #path('presence/list', get_presence_records, name='get_presence_records'),
    path('presence_records/<int:student_id>/', get_presence_records, name='get_presence_records'),
    path('presence_records/edit/<int:record_id>/', edit_presence_record, name='edit_presence_record'),
    path('presence_records/delete/<int:record_id>/', delete_presence_record, name='delete_presence_record'),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
