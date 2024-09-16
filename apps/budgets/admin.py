from django.contrib import admin
from .models import Budget

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ['user', 'category', 'limit', 'start_date', 'end_date']
    list_filter = ['start_date', 'end_date', 'category']
    search_fields = ['user__username', 'category__name']
