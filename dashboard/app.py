# dashboard/apps.py

from django.apps import AppConfig
import dashboard.signals as signals

class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'

    def ready(self):
         signals