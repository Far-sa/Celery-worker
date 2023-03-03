from django.urls import path

from . import views


urlpatterns = [
    path("notify-email/", views.notification_mail, name="notify-email"),
    path("schedule-email/", views.schedule_email, name="schedule-email"),
]
