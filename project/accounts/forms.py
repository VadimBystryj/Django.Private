from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMultiAlternatives, mail_managers, mail_admins
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)




        subject = 'Добро пожаловать в наш интернет магазин! '
        text = f'{user.username}, вы успешно зарегистрировались!'
        html = (
            f'<b>{user.username}</b>, вы успешно зарениситрировались на '
            f'<a href="http://127.o.o.1:8000/news/search">сайте</a>!'
        )
        msg = EmailMultiAlternatives(subject=subject, body=text, from_email=None, to=[user.email])
        msg.attach_alternative(html, "text/html")
        msg.send()
        mail_managers(
            subject='Новый пользователь!',
            message=f'Пользователь {user.username} зарегистрировался на сайте.'
        )
        mail_admins(
            subject='Новый пользователь!',
            message=f'Пользователь {user.username} зарегистрировался на сайте.'
        )

        return user