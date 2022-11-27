from django.contrib import admin
from django.contrib import admin
from .models import *


class UsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'avatar', 'is_staff', 'is_active', 'last_login']
    search_fields = ['first_name', 'last_name']


# Register your models here.
admin.site.register(User, UsersAdmin)
