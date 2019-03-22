import os
from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField

fs = FileSystemStorage(location='blog/static/media')

# Create your models here.

class Attachments(models.Model):
    caption = models.CharField(max_length=150)
    theFile = models.FileField(upload_to='attach/', storage=fs)
    thePost = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True)
    Create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"


class Post(models.Model):
    title = models.CharField(max_length=200)
    alias = models.CharField(max_length=70, unique=True)
    logo = models.ImageField(upload_to='logos/', storage=fs, blank=True)
    text = RichTextField()
    more = RichTextField(blank=True)
    pinn = models.BooleanField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, default=0)
    tags = models.ManyToManyField('Tag', null=True, blank=True)
    create_date = models.DateTimeField(default=timezone.now)

    # overrides entry title everywhere
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

class Sections(models.Model):
    TEMPLATES_TYP = {
        ('img','Image Galary'),
        ('cat','App Catalog'),
    }
    Title = models.CharField(max_length=200)
    Alias = models.CharField(max_length=70, unique=True)
    Kind = models.CharField(choices=TEMPLATES_TYP, default='cat', max_length=3)
    Description = models.TextField()

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"

class Category(models.Model):
    Name = models.CharField(max_length=200)
    Alias = models.CharField(max_length=70, unique=True)
    Section = models.ForeignKey('Sections', on_delete=models.SET_NULL, null=True, blank=True)
    Description = models.TextField(blank=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Tag(models.Model):
    Name = models.CharField(max_length=200)
    Alias = models.CharField(max_length=70, unique=True)
    Description = models.TextField(blank=True)
    Section = models.ForeignKey('Sections', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

class Presentation(models.Model):
    SECTIONS = {
        (0, 'Proclamation'),
        (1, 'Advantages'),
        (2, 'Partners'),
    }
    Title = models.CharField(max_length=150)
    Cover = models.ImageField(upload_to='pres/', storage=fs, null=True, verbose_name='Image (Procla=bitmap, Advance=svg, Partner=banner)')
    Text = models.TextField();
    Kind = models.IntegerField(choices=SECTIONS, default=0)
    Link = models.URLField()

    class Meta:
        verbose_name = "Презентация"
        verbose_name_plural = "Презентации"

    def __str__(self):
        return self.Title