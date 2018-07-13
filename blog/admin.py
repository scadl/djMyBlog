from django.contrib import admin
from .models import *

class SettingsAdmin(admin.ModelAdmin):
    list_display = ('Blog_Title', 'Create_date', 'Is_Active')
    ordering = ['-Create_date']
    pass

class AliedAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Alias')
    pass

# Register your models here.
admin.site.register(Post)
admin.site.register(Category, AliedAdmin)
admin.site.register(Setting, SettingsAdmin)
admin.site.register(Tag, AliedAdmin)
admin.site.register(Pages, AliedAdmin)

