# Generated by Django 2.1.7 on 2019-03-12 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20190312_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Category'),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='Section',
            field=models.IntegerField(choices=[(1, 'Advantages'), (0, 'Proclamation'), (2, 'Partners')]),
        ),
    ]