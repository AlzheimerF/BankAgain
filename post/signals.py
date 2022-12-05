from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Post, Order
from user.models import Profile

@receiver(signal=post_save, sender=Post)
def create_some_info(sender, **kwargs):
    order = Order.objects.create(
        post=kwargs.get('instance'),
        type_order=kwargs.get('instance').type_post,
        user_owner=Profile.objects.get(id=kwargs.get('instance').user.id),
    )
    order.save()
    return order
