from django.urls import path, include
from .views import JobListView

urlpatterns = [
    path('joblist/', JobListView.as_view(), name='joblist'),
]
