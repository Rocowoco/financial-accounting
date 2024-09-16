from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'name']
    search_fields = ['name', 'user__username']
    list_filter = ['user']
