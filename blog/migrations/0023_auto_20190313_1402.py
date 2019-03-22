# Generated by Django 2.1.7 on 2019-03-13 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20190313_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Alias', models.CharField(max_length=70, unique=True)),
                ('TemplateTyp', models.CharField(choices=[('img', 'Image Galary'), ('cat', 'App Catalog')], default='cat', max_length=3)),
                ('Description', models.TextField()),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
            },
        ),
        migrations.RemoveField(
            model_name='category',
            name='TemplateTyp',
        ),
        migrations.AddField(
            model_name='tag',
            name='Description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='Description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='Kind',
            field=models.IntegerField(choices=[(0, 'Proclamation'), (2, 'Partners'), (1, 'Advantages')], default=0),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='Text',
            field=models.TextField(),
        ),
        migrations.AddField(
            model_name='category',
            name='Section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Sections'),
        ),
        migrations.AddField(
            model_name='tag',
            name='Section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Sections'),
        ),
    ]
