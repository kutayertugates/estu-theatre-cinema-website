from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Admin listeleme ekranında görünecek sütunlar
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    
    # Listeleme ekranında hangi alana tıklayınca detay açilsin
    list_display_links = ('email',)
    
    # Arama çubuğu hangi alanlarda arama yapsın
    search_fields = ('email', 'first_name', 'last_name')
    
    # Listeleme ekranında varsayılan sıralama
    ordering = ('email',)

    # --- KRİTİK AYARLAR ---
    
    # 1. Kullanıcı Düzenleme Ekranı (Edit User)
    # Standart User modelinde 'username' olduğu için buraları ezmemiz lazım.
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Kişisel Bilgiler', {'fields': ('first_name', 'last_name')}),
        ('Yetkiler', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Önemli Tarihler', {'fields': ('last_login', 'date_joined')}),
    )

    # 2. Yeni Kullanıcı Ekleme Ekranı (Add User)
    # Admin panelinden "Kullanıcı Ekle" dediğinde çıkacak form.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'confirm_password'), # confirm_password'ü UserAdmin otomatik halleder
        }),
    )

    # filter_horizontal, ManyToMany alanlar (Grup ve Yetkiler) için şık bir seçim kutusu sağlar
    filter_horizontal = ('groups', 'user_permissions',)