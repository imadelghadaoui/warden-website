# signals.py

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import PresenceRecords
import logging
from .views import aggregate_and_update_attendance

logger = logging.getLogger(__name__)

@receiver(post_save, sender=PresenceRecords)
@receiver(post_delete, sender=PresenceRecords)

def update_attendance_on_presence_change(sender, instance, **kwargs):
 
    aggregate_and_update_attendance()
    logger.info(f"Attendance updated due to PresenceRecords change: {instance}")
