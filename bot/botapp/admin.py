from django.contrib import admin
from . import models
# Register your models here.
from .models import Words


class Admin(admin.ModelAdmin):
    list_display = ['pk', 'gender', 'word']
    list_editable = ['gender', 'word']

admin.site.register(models.Words, Admin)