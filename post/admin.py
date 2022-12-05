from django.contrib import admin
from .models import Post, Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_order', 'status', 'user_owner', 'user_client', 'datetime')

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'summ', 'currency', 'datetime')



admin.site.register(Order, OrderAdmin)
admin.site.register(Post, PostAdmin)