from django.contrib import admin
from .models import Room

class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'name', 'slug')

admin.site.register(Room, RoomAdmin)

