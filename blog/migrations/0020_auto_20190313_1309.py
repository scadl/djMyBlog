# Generated by Django 2.1.7 on 2019-03-13 10:09

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20190313_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='Cover',
            field=models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(location='blog/static/media'), upload_to='pres/', verbose_name='Image<br>Procla=bitmap,<br>Advance=svg,<br>Partner=banner'),
        ),
    ]
