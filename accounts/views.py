from django.shortcuts import render
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.contrib import messages
from accounts.models import Token
from django.core.urlresolvers import reverse
from django.contrib import auth, messages
# Create your views here.


def send_login_email(request):
    email = request.POST['email']
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(
        reverse('login') + '?token=' + str(token.uid)
    )
    message_body = "Use this link to log in: \n\n{}".format(url)
    send_mail(
        'Your login link for Superlists',
        message_body,
        'noreply@superlists',
        [email])
    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in."
    )
    return redirect('/')


def login(request):
    user = auth.authenticate(uid=request.GET.get('token'))
    if user:
        auth.login(request, user)
    return redirect('/')
