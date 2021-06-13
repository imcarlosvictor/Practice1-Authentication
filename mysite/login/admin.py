from django.contrib import admin
from django.contrib.admin import SimpleListFilter

from .models import Person


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


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'gender', 'email',
                    'date_created')
    list_filter = ('gender', EmailFilter)
    ordering = ('-last_name', )
    search_fields = ['last_name', 'first_name']
