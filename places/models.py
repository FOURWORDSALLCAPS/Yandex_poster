from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = HTMLField('Длинное описание', blank=True)
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    order = models.IntegerField(default=0, verbose_name='Очередность')
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Место'
    )
    imgs = models.ImageField('Картинка', upload_to='media/')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.order} {self.place.title}'
