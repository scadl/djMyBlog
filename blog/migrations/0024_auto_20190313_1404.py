# Generated by Django 2.1.7 on 2019-03-13 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20190313_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='Kind',
            field=models.IntegerField(choices=[(2, 'Partners'), (0, 'Proclamation'), (1, 'Advantages')], default=0),
        ),
        migrations.AlterField(
            model_name='sections',
            name='TemplateTyp',
            field=models.CharField(choices=[('cat', 'App Catalog'), ('img', 'Image Galary')], default='cat', max_length=3),
        ),
    ]