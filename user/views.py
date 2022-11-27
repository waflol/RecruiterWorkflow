from http.client import HTTPResponse

from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
def home(request):
    if request.method == 'GET':
        return render(request, 'homepage/home.html')
    return HttpResponse("BAD REQUEST", status=400)


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect('/login')

