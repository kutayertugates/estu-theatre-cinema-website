from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Department

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'tc_no', 'phone', 'period')

    list_filter = ('period',)
    
    search_fields = ('email', 'first_name', 'last_name')
    
    ordering = ('email',)

    fieldsets = (
        ('Dönem', {'fields': ('period',)}),
        ('Temel', {'fields': ('email', 'password')}),
        ('Kişisel Bilgiler', {'fields': ('first_name', 'last_name', 'tc_no', 'phone', 'department')}),
        ('Dosyalar', {'fields': ('receipt',)}),
        ('Yetkiler', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Önemli Tarihler', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'fields': ('period', 'email', 'password1', 'password2'),
        }),
    )

    filter_horizontal = ('groups', 'user_permissions',)

@admin.register(Department)
class DepartmentModel(admin.ModelAdmin):
    list_display = ('faculty', 'department',)

    list_filter = ('faculty',)
    
    search_fields = ('faculty', 'department',)

    fieldsets = (
        (None, {
            'fields': ('faculty', 'department')
        }),
    )

    add_fieldsets = (
        (None, {
            'fields': ('faculty', 'department'),
        }),
    )