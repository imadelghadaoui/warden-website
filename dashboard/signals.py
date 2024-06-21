# signals.py

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import PresenceRecords
from .views import aggregate_and_update_attendance

@receiver([post_save, post_delete], sender=PresenceRecords)
def update_attendance_on_presence_change(sender, instance, **kwargs):
    
    aggregate_and_update_attendance()