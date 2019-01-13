from django.db import models
import datetime
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


class Shift(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    clock_in = models.DateTimeField(blank=True, null=True)
    clock_out = models.DateTimeField(blank=True, null=True)  
    date = models.DateField(blank=True, null=True)
    duration  = models.FloatField(default=0)
    break_time = models.DurationField(blank=True, null=True)
    description = models.TextField(blank=True, null=True, max_length=140)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if self.clock_out and self.clock_in:
            self.duration = (self.clock_out - self.clock_in).seconds/60/60
            if self.break_time:
                self.duration = self.duration - self.break_time.seconds/60/60
                self.duration = round(self.duration, 1)
        else:
            return
        super(Shift, self).save(*args, **kwargs)
