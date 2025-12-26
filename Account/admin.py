from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('tc_no', 'email', 'first_name', 'last_name', 'phone', 'is_active')
    
    list_display_links = ('email',)
    
    search_fields = ('email', 'first_name', 'last_name')
    
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Kişisel Bilgiler', {'fields': ('first_name', 'last_name')}),
        ('Dosyalar', {'fields': ('receipt',)}),
        ('Yetkiler', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Önemli Tarihler', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'fields': ('email', 'password', 'confirm_password'),
        }),
    )

    filter_horizontal = ('groups', 'user_permissions',)