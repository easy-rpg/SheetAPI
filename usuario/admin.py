from django.contrib import admin
from .models import PerfilUsuario
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import User


class UserProfileInline(admin.TabularInline):
    model = PerfilUsuario


class UserAdmin(DjangoUserAdmin):
    inlines = (UserProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

