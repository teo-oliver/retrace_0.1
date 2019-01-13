from django.db import models
from django.utils import timezone


class Task(models.Model):
    text = models.CharField(max_length=40)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text