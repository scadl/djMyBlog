# Generated by Django 2.1.3 on 2018-11-24 12:39

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180712_1122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='setting',
            options={'verbose_name': 'Шаблон', 'verbose_name_plural': 'Шаблоны'},
        ),
        migrations.AddField(
            model_name='setting',
            name='Welcome_Mesage',
            field=models.TextField(default='Hello, Guest!'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='Blog_Logo',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='blog/static/media'), upload_to='logos/'),
        ),
    ]
