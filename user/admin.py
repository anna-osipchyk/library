from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from user.models import User


class CustomUserAdmin(UserAdmin):
    model = User

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_manager', 'username')}),
    )


admin.site.register(User, UserAdmin)
