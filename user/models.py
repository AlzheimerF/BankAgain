from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from django.contrib.auth.base_user import BaseUserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings

# from django_rest_passwordreset.signals import reset_password_token_created

class MyUserManager(BaseUserManager):
    def _create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError("Вы не ввели Email")
        if not username:
            raise ValueError("Вы не ввели Логин")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password):
        return self._create_user(email, username, password)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(' is_superuser=True.')

        return self._create_user(
            username=username,
            password=password,
            **extra_fields
        )

class Profile(AbstractUser):
    about_yourself = models.TextField(null=True)
    email_verify = models.UUIDField(default=uuid4())
    email = models.EmailField(max_length=250, unique=True)

    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'  # Идентификатор для обращения
    REQUIRED_FIELDS = ['username']  # Список имён полей для Superuser

    objects = MyUserManager()

    def str(self):
        return f'{self.username, self.email_verify}'

    def email_verificate(self):
        self.is_active = True
        self.save(update_fields=['is_active'])

@receiver(post_save, sender=Profile)
def create_profile(sender, instance, created, **kwargs):
    if created:
        uuid = instance.email_verify
        send_mail('Contact Form',
                  f'http://127.0.0.1:8000/email/verification/{uuid}',
                  settings.EMAIL_HOST_USER,
                  [instance.email],
                  fail_silently=False)





class Info(models.Model):
    LANGUAGE_CHOICES = [
        ('English', 'English'),
        ('Russian', 'Russian'),
    ]
    GENDER_CHOICES = [
        ('Female', 'Female'),
        ('Male', 'Male'),
    ]
    user = models.OneToOneField(Profile, on_delete=models.PROTECT, related_name='info')
    avatar = models.ImageField(null=True)
    country = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)

    def __str__(self):
        return self.user.username

class SecretInfo(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.PROTECT, related_name='secret_info')
    passport_front = models.ImageField(null=True)
    passport_back = models.ImageField(null=True)
    address = models.CharField(max_length=255, null=True)
    number = models.BigIntegerField(null=True)

    def __str__(self):
        return self.user.username

class Rate(models.Model):
    STARS_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    user = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='user')
    user_who_rate = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='user_who_rate')
    stars = models.IntegerField(choices=STARS_CHOICES)
    image = models.ImageField()
    text = models.TextField()

    def __str__(self):
        return str(self.stars) + ' Stars'

