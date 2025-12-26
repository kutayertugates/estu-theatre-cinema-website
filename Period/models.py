from django.db import models

class Period(models.Model):
    start_year = models.PositiveIntegerField(verbose_name="Başlangıç Yılı")
    finish_year = models.PositiveIntegerField(verbose_name="Bitiş Yılı")

    class Meta:
        verbose_name = 'Dönem'
        verbose_name_plural = 'Dönemler'
    
    def __str__(self):
        return f'{self.start_year}-{self.finish_year}'