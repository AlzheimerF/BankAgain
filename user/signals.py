from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from .models import Profile
from django.conf import settings

