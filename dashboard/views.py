from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View


# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


class CalendarView(View):
    def get(self, request):
        context = {}
        return render(request, 'dashboard/calendar.html', context)


class CandidateView(View):
    def get(self, request):
        return render(request, 'dashboard/candidate/candidate_list.html')


def add_email(request):
    return render(request, 'dashboard/mail/add_mail.html')


def list_email(request):
    return render(request, 'dashboard/mail/mail_list.html')
