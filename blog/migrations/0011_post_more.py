# Generated by Django 2.1.7 on 2019-03-12 12:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190312_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='more',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
