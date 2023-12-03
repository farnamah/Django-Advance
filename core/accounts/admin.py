from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile


# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_superuser', 'is_active')
    list_filter = ('email', 'is_superuser', 'is_active')
    searching_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        ("Authentication", {
            "fields": (
                'email', 'password'
            ),
        }),
        ('permissions', {
            "fields": (
                'is_staff', 'is_active', "is_superuser"
            ),
        }),
        ('important date', {
            "fields": ('last_login',),
        }),
        ('Group Permissions', {
            "fields": (
                'group', 'user_permissions'
            ),
        }),
    )

    add_fieldsets = (
        (None, {
            "classes": ('wide',),
            "fields": ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser')
        }),
    )


admin.site.register(Profile)
admin.site.register(User, CustomUserAdmin)
