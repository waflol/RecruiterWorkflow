from django.urls import path
from .views import dashboard, CandidateView, CalendarView, add_email, list_email

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('candidatelist/', CandidateView.as_view(), name='candidatelist'),
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('addemail/', add_email, name='addemail'),
    path('emaillist/', list_email, name='emaillist'),
]
