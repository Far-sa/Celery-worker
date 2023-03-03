from __future__ import absolute_import, unicode_literals
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils import timezone
from datetime import timedelta

from celery import shared_task

User = get_user_model()


@shared_task(bind=True)
def send_mail_func(self):
    users = User.objects.all()
    # timezone.localtime(users.date_time) + timedelta(days=2)
    for user in users:
        mail_subject = "Hey Guys! Welcome to my shop"
        message = "If you like my Products,Please do not hesitate to buy"
        to_email = user.email
        send_mail(subject=mail_subject, message=message, from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[to_email], fail_silently=True)

    return "Task Done"

# TODO create a task for verify user email


@shared_task(bind=True)
def email_verify(self):
    return "Task Done"
