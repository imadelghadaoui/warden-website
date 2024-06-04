from django.contrib import admin
from .models import ContactFormSubmission

@admin.register(ContactFormSubmission)
class ContactFormSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone' ,'message' ,'created_at')
    search_fields = ('name', 'email', 'phone')
