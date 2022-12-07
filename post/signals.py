from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Post, Order
from user.models import Profile

# @receiver(signal=post_save, sender=Post)
# def create_order(sender, **kwargs):
#     # post = Post.objects.get(id=kwargs.get('instance').id)
#     # post.percent = post.percent / 100
#     # post.save()
#     order = Order.objects.create(
#         post=kwargs.get('instance'),
#         type_order=kwargs.get('instance').type_post,
#         user_owner=Profile.objects.get(id=kwargs.get('instance').user.id),
#     )
#     order.save()
#     return order





