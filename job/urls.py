from django.urls import path, include
from .views import JobListView, AddJobView

urlpatterns = [
    path('joblist/', JobListView.as_view(), name='joblist'),
    path('addjob/', AddJobView.as_view(), name='addjob'),
]
