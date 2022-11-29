from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from user.forms import RegisterForm
from user.models import User


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'authentication/register/register.html', {'form': RegisterForm()})

    def post(self, request):
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            return HttpResponse('CONFLICT', status=409)

        user = User.objects.create_user(username=email, email=email, first_name=first_name, last_name=last_name,
                                        password=password, is_active=False)
        current_site = get_current_site(request)
        current_site.domain = '127.0.0.1:8000'
        mail_subject = 'Please activate your account'
        message = render_to_string('authentication/register/account_verification_email.html', {
            'user': user,
            'domain': current_site,
            'uid': urlsafe_base64_encode(force_bytes(user.id)),
            'token': default_token_generator.make_token(user),
        })
        send_email = EmailMessage(mail_subject, message, to=[email])
        send_email.content_subtype = 'html'
        send_email.fail_silently = True
        success = send_email.send()
        if success == 0:
            return HttpResponse('NOT FOUND', status=404)
        return HttpResponse('CREATED', status=201)


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(id=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated.')
    else:
        messages.error(request, 'Invalid activation link')
    return redirect('login')
