from django.contrib import admin
from .models import JobCategory, JobType

# Register your models here.
admin.site.register(JobCategory)
admin.site.register(JobType)
