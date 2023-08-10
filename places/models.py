from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Краткое описание')
    description_long = models.TextField('Длинное описание')
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField('Название', max_length=200)
    imgs = models.ImageField('Картинка', upload_to='images/')

    def __str__(self):
        return self.title
