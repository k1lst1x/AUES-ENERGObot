from django.contrib import admin

from . import models

class TextAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'text', 'translation']
    list_editable = ['name', 'text', 'translation']

admin.site.register(models.Texts, TextAdmin)