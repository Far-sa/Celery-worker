from django.http import HttpResponse
from django_celery_beat.models import PeriodicTask, CrontabSchedule

from .tasks import send_mail_func
# Create your views here.

#! worng fn


def notification_mail(request):
    send_mail_func.delay()
    return HttpResponse("Email has been sent")


def schedule_email(request):
    schedule, created = CrontabSchedule.objects.get_or_create(
        hour=18, minute=36)
    task = PeriodicTask.objects.create(
        crontab=schedule, name="schedule_email"+"1", task="send_mail.tasks.send_mail_func")
    return HttpResponse("Schedule Email has been set")
