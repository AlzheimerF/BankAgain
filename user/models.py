from django.db import models
from django.contrib.auth.models import AbstractUser

class Profile(AbstractUser):
    # CREDIT_CHOICES = [
    #     ('Giving', 'Giving'),
    #     ('Taking', 'Taking'),
    # ]
    # status = models.CharField(default=None, choices=CREDIT_CHOICES, max_length=50, null=True)
    # # date_joined = models.DateTimeField(auto_now_add=True)
    about_yourself = models.TextField(null=True)

    def __str__(self):
        return self.username


class Info(models.Model):
    LANGUAGE_CHOICES = [
        ('English', 'English'),
        ('Russian', 'Russian'),
    ]
    GENDER_CHOICES = [
        ('Female', 'Female'),
        ('Male', 'Male'),
    ]
    user = models.ForeignKey(Profile, on_delete=models.PROTECT)
    avatar = models.ImageField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return self.country

class SecretInfo(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.PROTECT)
    passport_front = models.ImageField(unique=True)
    passport_back = models.ImageField(unique=True)
    address = models.CharField(max_length=255, unique=True)
    number = models.BigIntegerField(null=True, unique=True)

    def __str__(self):
        return self.address

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

