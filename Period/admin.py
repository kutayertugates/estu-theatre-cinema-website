from django.contrib import admin
from .models import Period

@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'start_year', 'finish_year')
    search_fields = ('start_year', 'finish_year')
    ordering = ('-start_year',)
    fields = ('start_year', 'finish_year')
