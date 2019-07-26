import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mac.settings.dev")

app = Celery("mac")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

