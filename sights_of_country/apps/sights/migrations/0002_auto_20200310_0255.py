# Generated by Django 3.0.3 on 2020-03-09 23:55

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sights', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='sights_of_country/apps/sights/media/images'), upload_to='', verbose_name='изображение объекта'),
        ),
    ]
