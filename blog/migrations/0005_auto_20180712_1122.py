# Generated by Django 2.0.7 on 2018-07-12 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180711_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='Blog_Logo',
            field=models.FileField(upload_to='logos/'),
        ),
    ]