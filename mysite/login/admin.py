from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.contrib.auth.models import User


# Register your models here.
class EmailFilter(admin.SimpleListFilter):
    """Custom filter for finding users with no email."""

    title = 'Email Filter'
    parameter_name = 'email'

    def lookups(self, request, model_admin):
        return (
            ('has_email', 'has_email'),
            ('no_email', 'no_email'),
        )

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value().lower() == 'has_email':
            return queryset.exclude(email='')
        if self.value().lower() == 'no_email':
            return queryset.filter(email='')


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'last_name', 'first_name', 'email',
                    'is_staff', 'date_joined')
    list_filter = ('is_staff', EmailFilter)
    ordering = ('-last_name', )
    search_fields = ['username']
