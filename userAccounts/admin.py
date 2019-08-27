from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import User


class customUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        (None , {'fields':('profile','college','level')}),
    )
    list_display = ('username','email','profile','college','level')

admin.site.register(User , customUserAdmin)