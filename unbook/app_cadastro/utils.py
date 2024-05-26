# myapp/utils.py

from django.core.mail import send_mail

from django.template.loader import render_to_string

from django.utils.http import urlsafe_base64_encode

from django.utils.encoding import force_bytes

from django.contrib.auth.tokens import default_token_generator

from django.urls import reverse


def send_activation_email(user, request):

    token = default_token_generator.make_token(user)

    uid = urlsafe_base64_encode(force_bytes(user.pk))
    link_ativacao = request.build_absolute_uri(reverse('verificar', kwargs={'uidb64': uid, 'token': token}))


    subject = 'Ative sua conta'

    message = render_to_string('html/email_ativacao.html', {'link_ativacao': link_ativacao})

    send_mail(subject, message, 'django.core.mail.backends.console.EmailBackend', [user.email])

