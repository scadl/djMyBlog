import os
from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField

fs = FileSystemStorage(location='blog/static/media')

# Create your models here.

class Setting(models.Model):
    Blog_Title = models.CharField(max_length=100)
    Blog_Description = models.CharField(max_length=200)
    Blog_Logo = models.ImageField(upload_to='logos/', storage=fs)
    Create_date = models.DateTimeField(default=timezone.now)
    Header_Background = ColorField(default='#CCCCCC')
    Header_Text_Color = ColorField(default='#FFFFFF')
    Titles_Color = ColorField(default='#CCCCCC')
    Is_Active = models.BooleanField(default=False)
    Welcome_Mesage = RichTextField(default='Hello, Guest!')

    # Alternative @Save method (able to mimiqe UNIQUE key):
    # if isActive = True, check over fields with same isActive
    # All fields, who has isActive = True,
    # but differend other fields, recives isActive=False
    def save(self, *args, **kwargs):
        if self.Is_Active:
            try:
                oset = Setting.objects.get(Is_Active=True)
                if self != oset:
                    oset.Is_Active = False
                    oset.save()
            except Setting.DoesNotExist:
                pass

        super(Setting, self).save(*args, **kwargs)

    def __str__(self):
        return self.Blog_Title

    class Meta:
        verbose_name = "Шаблон"
        verbose_name_plural = "Шаблоны"


class Post(models.Model):
    title = models.CharField(max_length=200)
    alias = models.CharField(max_length=70, unique=True)
    text = RichTextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    create_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    # overrides entry title everywhere
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Посты"
        verbose_name_plural = "Пост"

class Category(models.Model):
    Name = models.CharField(max_length=200)
    Alias = models.CharField(max_length=70, unique=True)
    Description = models.TextField()

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категория"

class Tag(models.Model):
    Name = models.CharField(max_length=200)
    Alias = models.CharField(max_length=70, unique=True)
    Description = models.TextField()

    class Meta:
        verbose_name = "Тэги"
        verbose_name_plural = "Тэг"

class Pages(models.Model):
    Name = models.CharField(max_length=200)
    Alias = models.CharField(max_length=70, unique=True)
    Page_Text = models.TextField()
    Page_Date = models.DateTimeField()

    class Meta:
        verbose_name = "Страницы"
        verbose_name_plural = "Страница"