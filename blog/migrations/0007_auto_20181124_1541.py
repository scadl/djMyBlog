# Generated by Django 2.1.3 on 2018-11-24 12:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20181124_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='Welcome_Mesage',
            field=ckeditor.fields.RichTextField(default='Hello, Guest!'),
        ),
    ]