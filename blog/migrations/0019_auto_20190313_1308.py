# Generated by Django 2.1.7 on 2019-03-13 10:08

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20190312_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='Cover',
            field=models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(location='blog/static/media'), upload_to='pres/', verbose_name='Image\nProcla=bitmap,\nAdvance=svg,\nPartner=banner'),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='Kind',
            field=models.IntegerField(choices=[(1, 'Advantages'), (2, 'Partners'), (0, 'Proclamation')], default=0),
        ),
    ]
