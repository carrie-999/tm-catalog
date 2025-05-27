from django.contrib import admin
from .models import NameRegistration

@admin.register(NameRegistration)
class NameRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'country', 'postal_code', 'user', 'created_at')
    list_filter = ('status', 'country', 'user')
    search_fields = ('name', 'postal_code', 'user__username')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
