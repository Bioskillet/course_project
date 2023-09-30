from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'datetime', 'server')
    list_filter = ('server', 'datetime')


admin.site.register(Item, ItemAdmin)
