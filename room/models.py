from django.db import models
from user.models import Profile
from post.models import Order

class Room(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.PROTECT)
    user = models.ForeignKey(Profile, related_name='messages', on_delete=models.PROTECT)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added', )