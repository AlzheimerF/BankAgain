from django.test import TestCase
from . import models

class TestOne(TestCase):

    def setUp(self):
        order = models.Room.objects.create(
            order=,
            name='Room1',
            slug='123'
        )

    def test_room(self):
        self.assertEqual(1, int(models.Room.objects.get(id=1).id))