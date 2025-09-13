from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import users

@admin.register(users)
class CustomUserAdmin(UserAdmin):
    # These fields will show in the admin list view
    list_display = ("username", "email", "is_staff", "is_active",)
    list_filter = ("is_staff", "is_active")
    search_fields = ("username", "email")
    ordering = ("username",)


# Register your models here.
