from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from user.forms import LoginForm
from django.http import HttpResponse


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'authentication/login/login.html', {'form': LoginForm()})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        email = request.POST['email']
        password = request.POST['password']
        check_user = authenticate(username=email, password=password)
        if check_user is None:
            return HttpResponse('BAD REQUEST', status=400)
        login(request, check_user)
        return HttpResponse('Success', status=200)
