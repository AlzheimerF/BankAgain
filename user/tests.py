from django.test import TestCase
from . import models

class OneTest(TestCase):

    def setUp(self):
        self.user = models.Profile.objects.create_user(
            username='Alz1',
            email='1@gmail.com',
            password='azsxdcfv123'
        )

    def test_check_user(self):
        self.assertEqual(str(1), str(models.Profile.objects.count()))
        self.assertEqual('Alz1', models.Profile.objects.get(id=1).username)


