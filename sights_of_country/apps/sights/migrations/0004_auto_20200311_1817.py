# Generated by Django 3.0.3 on 2020-03-11 15:17

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sights', '0003_auto_20200311_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(base_url='/media', location='sights_of_country/media'), upload_to='images', verbose_name='изображение объекта'),
        ),
    ]
