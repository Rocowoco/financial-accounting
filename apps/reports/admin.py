from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['user', 'start_date', 'end_date']
    list_filter = ['start_date', 'end_date']
    search_fields = ['user__username']
