# Generated by Django 2.1.7 on 2019-03-12 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20190312_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='Kind',
            field=models.IntegerField(choices=[(2, 'Partners'), (1, 'Advantages'), (0, 'Proclamation')], default=0),
        ),
    ]