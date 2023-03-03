from __future__ import absolute_import, unicode_literals
from celery import Celery
import os
from celery.schedules import crontab

from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")


app = Celery("proj")

app.conf.enable_utc = False
app.conf.update(timezone="Asia/Istanbul")

app.config_from_object(settings, namespace="CELERY")

# Celery Beat Settings
app.conf.beat_schedule = {
    "send-weekly-mail-at-12": {
        "task": "send_mail.tasks.send_mail_func",
        "schedule": crontab(hour=12, minute=30),
        # "args":(2,)
    }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request : {self.request!r}")
