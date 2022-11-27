from django.db import models
from tag.models import JobType, JobCategory
from user.models import User
from dashboard.models import Candidate


# Create your models here.
class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    job_type = models.ManyToManyField(JobType, null=True, blank=True)
    recruit_number = models.PositiveIntegerField(default=0, null=True, blank=True)

    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

    category = models.ManyToManyField(JobCategory, null=True, blank=True)


class Step(models.Model):
    workflow = models.ForeignKey(Job, related_name='steps', on_delete=models.CASCADE)
    order_step = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    candidate = models.ManyToManyField(Candidate, blank=True, null=True)

    def __str__(self):
        return ''.join(self.order_step, '_', self.name)
