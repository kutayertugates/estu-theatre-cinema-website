from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from Account.managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    # period
    first_name = models.CharField(max_length=50, blank=True, verbose_name='Ad')
    last_name = models.CharField(max_length=50, blank=True, verbose_name='Soyad')
    email = models.EmailField(unique=True, verbose_name='Email Adresi')
    phone = models.CharField(max_length=24, blank=True, verbose_name='Telefon Numarası')
    tc_no = models.CharField(max_length=11, blank=True, verbose_name='Okul Numarası')
    # department
    receipt = models.FileField(upload_to='receipts/%Y/%m/', blank=True, null=True, verbose_name='Dekont Dosyası') 

    
    is_staff = models.BooleanField(default=False) # Admin paneline girebilir mi?
    is_active = models.BooleanField(default=True) # Hesabı aktif mi?
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Kullanıcı'
        verbose_name_plural = 'Kullanıcılar'

    def __str__(self):
        return self.email