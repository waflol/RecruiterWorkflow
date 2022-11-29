from django.urls import path
from .views import dashboard, CandidateView

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('candidatelist/', CandidateView.as_view(), name='candidatelist'),
]
