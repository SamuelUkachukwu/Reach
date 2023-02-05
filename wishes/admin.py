from django.contrib import admin
from .models import Item, Profile


# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
    )
    ordering = ('name',)
    search_fields = ('name', 'user')
    list_filter = ('name', 'user')


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'phone_number'
    )
    search_fields = ('name',)


admin.site.register(Item, ItemAdmin)
admin.site.register(Profile, ProfileAdmin)
