from django.db import models
from django.core.files.storage import FileSystemStorage
import PIL

from django.utils import timezone

fs = FileSystemStorage(location = 'sights_of_country/media')

class Sight(models.Model):
    sight_title = models.CharField('название объекта',max_length = 50)
    sight_description = models.TextField('описание объекта')
    sight_lat = models.FloatField('широта')
    sight_lon = models.FloatField('долгота')
    pub_date = models.DateTimeField('дата публикации',default=timezone.now())   

    def __str__(self):
        return self.sight_title

    class Meta():
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'

class Image(models.Model):
    sight = models.ForeignKey(Sight,on_delete = models.CASCADE)
    img = models.ImageField('изображение объекта',storage=fs)
    img_text = models.CharField('комментарии к изображению',max_length = 50)

    def __str__(self):
        return self.sight.sight_title

    class Meta():
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
