from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=2000, null=True)

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
    
    def __str__(self) -> str:
        return self.name

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.RESTRICT, verbose_name='Датчик', related_name='measurements')
    temperature = models.FloatField(verbose_name='Температура')
    created_at = models.DateTimeField(verbose_name='Дата и время', auto_now_add=True)
    image = models.ImageField(verbose_name='Изображение', null=True)

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'