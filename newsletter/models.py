from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from config import settings

# Create your models here.
class SubUsers(models.Model):

    email = models.EmailField(unique=True, blank=False, null=False)

    def __str__(self):
        return self.email

class newsletter(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return f'{self.title}'

@receiver(post_save, sender=newsletter)
def send_newsletter(sender, instance, created, **kwargs):
    if created:
        subject = instance.title
        message = instance.body

        send_mail(
            subject,
            message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email for user in SubUsers.objects.all()],
        )
    