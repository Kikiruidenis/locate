from django.contrib import admin
from . models import Lost,Found

class LostAdmin(admin.ModelAdmin):
    list_display = ('name','age','gender','complexion', 'child_pic', 'found')
    list_filter = ( 'found',)
    search_fields = ('name','found')

class FoundAdmin(admin.ModelAdmin):
    list_display = ('location', 'contact', 'videofile')
    list_filter = ( 'location',)
    search_fields = ('location','contact')

admin.site.register(Lost, LostAdmin)
admin.site.register(Found, FoundAdmin)
