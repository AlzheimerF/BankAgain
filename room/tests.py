from django.test import TestCase
from . import models

class TestOne(TestCase):

    def setUp(self):
        order = models.Room.objects.create(
            name='Room1',
            slug='123'
        )

    def test_room(self):
        self.assertFalse(models.Room.objects.count() < 0)
        self.assertTrue(models.Room.objects.count() < 6)
        self.assertEqual('Room1', models.Room.objects.get(id=1).name)
        self.assertNotEqual(models.Room.objects.count(), 2)
