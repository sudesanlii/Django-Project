from django.contrib import admin
from .models import ControlTable
# Register your models here.

class ControlAdmin(admin.ModelAdmin):
    
    list_display = ['cuet','uet','atolye','kritiklik']
    list_display_links = ['cuet','uet','atolye','kritiklik']
    list_filter=['atolye']
    search_fields=['cuet','kritiklik','atolye']
    
    class Meta:
        model=ControlTable

admin.site.register(ControlTable,ControlAdmin)