from django.db import models


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    location = models.CharField(max_length=255)
    start_time = models.TimeField(null=True, blank=True)
    start_date = models.DateField()
    end_time = models.TimeField(null=True, blank=True)
    end_date = models.DateField()


class Candidate(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    cv_file = models.FileField()
