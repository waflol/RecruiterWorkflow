from django.contrib.auth import logout
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.forms import ForgetForm, ResetPasswordForm
from user.models import User
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import get_template
from django.core.signing import Signer

signer = Signer(salt='extra')


def forgotPassword(request):
    if request.user.is_authenticated:
        return redirect('')
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact=email)

            # Reset password email
            current_site = get_current_site(request)
            current_site.domain = '127.0.0.1:8000'
            mail_subject = 'Reset Your Password'
            context_message = {
                'user': user,
                'domain': current_site,
                # 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'uid': signer.sign(int(user.pk)),
                'token': default_token_generator.make_token(user),
            }
            message = get_template('authentication/reset-password/email_reset_password.html').render(context_message)
            send_email = EmailMessage(mail_subject, message, to=[email])
            send_email.content_subtype = 'html'
            send_email.send(fail_silently=True)
            return HttpResponse('Password reset email has been sent to your email address.', status=200)
        else:
            return HttpResponse('Account does not exist!', status=400)
    return render(request, 'authentication/reset-password/forget_password.html', {'form': ForgetForm()})


def resetpassword_validate(request, uidb64, token):
    uid = None
    try:
        uid = int(signer.unsign(uidb64))
        user = User.objects.get(id=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uidb64'] = signer.sign(uid)
        messages.success(request, 'Please reset your password')
        return redirect('/resetPassword/')
    else:
        messages.error(request, 'This link has been expired!')
        return redirect('/login/')


def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = int(signer.unsign(request.session.get('uidb64')))
            user = User.objects.get(id=uid)
            user.set_password(password)
            user.save()
            if request.user.is_authenticated:
                logout(request)
            return HttpResponse('Password Changed', status=200)
        else:
            return HttpResponse('Not the same', status=400)
    else:
        return render(request, 'authentication/reset-password/new_password.html', {'form': ResetPasswordForm()})
