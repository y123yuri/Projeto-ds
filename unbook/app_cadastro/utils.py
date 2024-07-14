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
    print('gerei o token')
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    print('gerei o uid:', uid)
    try:
        reset_url = request.build_absolute_uri(
            reverse('novaSenha', kwargs={'uidb64': uid,'token': token})
        )
        print(reset_url,'consegui fazer o link de trocar')
    except Exception as e: 
        print('não consegui fazer o link de ativacao')
        raise e       

    subject = "Redefinição de senha"
    message = render_to_string('html/redefinicao.html', {
        'reset_url': reset_url
    })
    print(message, 'essa é a mensagem')
    try:
        send_mail(subject, message, 'unbook.br@gmail.com', [user.email])
        print('consegui enviar o email pra view')
    except Exception as e:
        print('nao consegui enviar o email pra view')
        raise e

def send_activation_email(user, request):

    token = default_token_generator.make_token(user)

    uid = urlsafe_base64_encode(force_bytes(user.pk))
    link_ativacao = request.build_absolute_uri(reverse('verificar', kwargs={'uidb64': uid, 'token': token}))


    subject = 'Ative sua conta'

    message = render_to_string('html/email_ativacao.html', {'link_ativacao': link_ativacao})

    send_mail(subject, message, 'django.core.mail.backends.console.EmailBackend', [user.email])

