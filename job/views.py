from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, CreateView
from .models import Job


# Create your views here.
class JobListView(View):
    def get(self, request):
        jobs = Job.objects.filter(user=request.user)
        context = {
            'jobs': jobs,
        }
        return render(request, 'dashboard/job/job_list.html', context)



