from django.db.models.signals import post_save
from django.dispatch import receiver
from . import models


@receiver(post_save, sender=models.Profile)
def add_info_and_s_info(sender, instance, created, **kwargs):
    if created:
        info = models.Info.objects.create(
            user=instance
        )
        secret_info = models.SecretInfo.objects.create(
            user=instance
        )
        info.save()
        secret_info.save()
        return info, secret_info
