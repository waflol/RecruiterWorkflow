from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View


# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


class CandidateView(View):
    def get(self, request):
        return render(request, 'dashboard/candidate/candidate_list.html')