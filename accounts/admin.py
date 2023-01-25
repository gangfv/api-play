from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth.models import Group

from .models import CustomUser


class AccountAdmin(BaseUserAdmin):
    list_display = ('email', 'name', 'phone', 'money', 'is_active', 'is_superuser')
    list_filter = ('is_superuser',)

    search_fields = ('email', 'name', 'phone', 'money')
    ordering = ('email',)
    filter_horizontal = ()

    fieldsets = (
        (None, {
            'fields': (
                'name', 'phone', 'city', 'email', 'password', 'money', 'is_active', 'is_superuser'
            )
        }),
    )

admin.site.register(CustomUser, AccountAdmin)
admin.site.unregister(Group)