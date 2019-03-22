# Generated by Django 2.1.7 on 2019-03-12 11:17

import ckeditor.fields
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190312_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=150)),
                ('theFile', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='blog/static/media'), upload_to='attach/')),
                ('Create_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
        ),
        migrations.DeleteModel(
            name='Pages',
        ),
        migrations.DeleteModel(
            name='Setting',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Записи', 'verbose_name_plural': 'Запись'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
        migrations.AddField(
            model_name='post',
            name='logo',
            field=models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(location='blog/static/media'), upload_to='logos/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AddField(
            model_name='post',
            name='attachments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Attachments'),
        ),
    ]
