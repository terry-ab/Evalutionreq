import os
from celery import Celery

# Set default settings module for Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'llm_evaluation.settings')

celery_app= Celery('llm_evaluation')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks in Django apps
celery_app.autodiscover_tasks()