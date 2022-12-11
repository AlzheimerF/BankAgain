from django.test import TestCase
from . import models

class UserTest(TestCase):

    def setUp(self):
        for i in range(5):
            self.user = models.Profile.objects.create_user(
                username=f'Alz1{i}',
                email=f'1{i}@gmail.com',
                password='azsxdcfv123'
            )
            i =+ 1

    def test_check_user(self):
        self.assertFalse(models.Profile.objects.count() < 1)
        self.assertTrue(models.Profile.objects.count() < 6)
        self.assertEqual('Alz10', models.Profile.objects.get(id=1).username)
        self.assertNotEqual(models.Profile.objects.count(), 2)

