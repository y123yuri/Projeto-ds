# myapp/utils.py

from django.core.mail import send_mail

from django.template.loader import render_to_string

from django.utils.http import urlsafe_base64_encode

from django.utils.encoding import force_bytes

from django.contrib.auth.tokens import default_token_generator

from django.urls import reverse

from django.utils.http import urlsafe_base64_encode

from django.template.loader import render_to_string
from django.core.mail import send_mail


def send_password_reset_email(user, request):
    token = default_token_generator.make_token(user)
    
    try:
        reset_url = request.build_absolute_uri(
            reverse('novaSenha', kwargs={'token': token})
        )
    except Exception as e: 
 
        raise e       

    subject = "Redefinição de senha"
    message = render_to_string('html/redefinição.html', {
        'user': user,
        'reset_url': reset_url
    })

    try:
        send_mail(subject, message, 'unbook.br@gmail.com', [user.email])
      
    except Exception as e:

        raise e

def send_activation_email(user, request):

    token = default_token_generator.make_token(user)

    uid = urlsafe_base64_encode(force_bytes(user.pk))
    link_ativacao = request.build_absolute_uri(reverse('verificar', kwargs={'uidb64': uid, 'token': token}))


    subject = 'Ative sua conta'

    message = render_to_string('html/email_ativacao.html', {'link_ativacao': link_ativacao})

    send_mail(subject, message, 'django.core.mail.backends.console.EmailBackend', [user.email])

