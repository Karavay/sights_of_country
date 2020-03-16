# Generated by Django 3.0.3 on 2020-03-16 12:45

import datetime
import django.core.files.storage
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sights', '0004_auto_20200311_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='sights_of_country/media'), upload_to='', verbose_name='изображение объекта'),
        ),
        migrations.AlterField(
            model_name='sight',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 12, 45, 39, 644527, tzinfo=utc), verbose_name='дата публикации'),
        ),
    ]