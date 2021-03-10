from django.db import models
from django import forms
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from blood.managers import UserManager
from django.utils.translation import ugettext_lazy as _

# Not using Django's own user class for 2 reasons:
# 1- I do not need a 'username'
# 2- I need the e-mail to be the auth token
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('e-mail'), null=False, blank=False, unique=True)
    full_name = models.CharField(_('full name'), null=False, blank=False, max_length=128)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    date_birth = models.DateField(_('date of birth'), null=True, blank=True)
    
    # Static gender list
    GENDERS = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('N', 'Nenhum destes/prefiro não informar'),
        ]
    gender = models.CharField(_('gender'), max_length=1, choices=GENDERS, null=False,  default='N')

    # Static blood types list
    BLOOD_TYPES = [
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-')
        ]
    blood_type = models.CharField(_('blood type'), max_length=3, choices=BLOOD_TYPES, null=False, default='AB+')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)