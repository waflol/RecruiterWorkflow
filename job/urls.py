from django.urls import path, include
from .views import JobListView, AddJobView, JobDetailView

urlpatterns = [
    path('joblist/', JobListView.as_view(), name='joblist'),
    path('addjob/', AddJobView.as_view(), name='addjob'),
    path('jobdetail/', JobDetailView.as_view(), name='jobdetail'),
]
