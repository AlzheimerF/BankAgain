from django.db import models
from user.models import Profile

class Post(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    CURRENCY_CHOICES = [
        ('EUR', 'EUR'),
        ('RUB', 'RUB'),
        ('US', 'US'),
        ('KZ', 'KZ'),
    ]
    TYPE_CHOICES = [
        ('Giving', 'Giving'),
        ('Taking', 'Taking'),
    ]
    type_post = models.CharField(choices=TYPE_CHOICES, max_length=200)
    title = models.CharField(max_length=255, )
    description = models.TextField()
    summ = models.IntegerField()
    percent = models.IntegerField()
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=50, )
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    term_of_conditions = models.IntegerField()
    status = models.BooleanField(null=True, default=False)

    def __str__(self):
        return str(self.title)



class Order(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post')
    type_order = models.CharField(max_length=200)
    user_owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner', null=True)
    user_client = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='client', null=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    STATUS_CHOICES = [
        ('IN ACTION', 'IN ACTION'),
        ('FINISHED', 'FINISHED'),
        ('CANCELED', 'CANCELED'),
    ]
    status = models.CharField(choices=STATUS_CHOICES, max_length=255, null=True)

    def __str__(self):
        return str(self.post.title)

