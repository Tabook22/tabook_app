from django.contrib import admin
from . models import Tabooksite

class TabooksiteAdmin(admin.ModelAdmin):
    list_display=['title','description']
# Register your models here.
admin.site.register (Tabooksite, TabooksiteAdmin)