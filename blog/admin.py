from django.contrib import admin
from .models import *

class AttachInline(admin.TabularInline):
    model = Attachments
    extra = 1
    min_num = 0
    pass

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','alias', 'category','create_date', 'pinn')
    inlines = [AttachInline]
    pass

class AliedAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Alias', 'Section')
    pass

class SectionAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Kind')
    pass

class AttachAdmin(admin.ModelAdmin):
    list_display = ('caption', 'thePost')

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, AliedAdmin)
admin.site.register(Attachments, AttachAdmin)
admin.site.register(Tag, AliedAdmin)
admin.site.register(Presentation, SectionAdmin)
admin.site.register(Sections, SectionAdmin)

