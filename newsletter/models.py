from django.db import models
from django.urls import reverse

# Create your models here.
class SubUsers(models.Model):

    email = models.EmailField(unique=True, blank=False, null=False)
    # is_active = models.BooleanField(default=True)
    subscribed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class newsletter(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('newsletter:det', args=(str(self.id)))