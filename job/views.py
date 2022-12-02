from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, CreateView
from .models import Job


# Create your views here.
class JobListView(LoginRequiredMixin, View):
    def get(self, request):
        jobs = Job.objects.filter(user=request.user)
        context = {
            'jobs': jobs,
        }
        return render(request, 'dashboard/job/job_list.html', context)


class AddJobView(LoginRequiredMixin, View):
    def get(self, request):
        context = {}
        return render(request, 'dashboard/job/add_job.html', context)

    def post(self, request):
        pass


class JobDetailView(LoginRequiredMixin, View):
    def get(self, request):
        context = {}
        return render(request, 'dashboard/job/job_detail.html', context)
